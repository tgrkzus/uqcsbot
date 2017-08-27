from errbot import BotPlugin, botcmd
import requests
import re
from bs4 import BeautifulSoup

class Whatsdue(BotPlugin):
    def get_channel_name(self, message):
        cID = message.extras.get('slack_event').get('channel')
        name = self._bot.channelid_to_channelname(cID)

        # If no channel name was found we're in a DM
        if cID == name:
            raise ValueError("Can't dm")
        return name

    def get_assessment(self, course):
        courseUrl = "https://www.uq.edu.au/study/course.html?course_code="
        assessmentUrl = "https://www.courses.uq.edu.au/student_section_report.php?report=assessment&profileIds="
    
        res = requests.get(courseUrl + course)

        if res.status_code != 200:
            raise ValueError("Invalid Course")

        # Find profile id
        try:
            profile = re.search("profileId=\d*", res.text).group(0).replace("profileId=", "")
        except AttributeError:
            raise ValueError("Invalid course")

        resAssignments = requests.get(assessmentUrl + profile)

        if resAssignments.status_code != 200:
            raise ValueError("Error in profile id")
        
        return self.parse_assignments(resAssignments.text)


    def parse_assignments(self, html):
        soup = BeautifulSoup(html, 'html.parser')

        # Get first table within the content div
        table = soup.find(id="content").find("table")

        # Get all table rows except for the first (which is the header)
        rows = table.findAll("tr")[1:-1]
        
        data = []

        for r in rows:
            cells = r.findAll("td")
            name = ""
            due = ""
            weight = ""

            for s in cells[1].find("div").strings:
                name += s.strip() + ' - '
            name = name[0:-3].strip()

            for s in cells[2].find("div").strings:
                due += s.strip() + ' - '
            due = due[0:-3].strip()

            for s in cells[3].find("div").strings:
                weight += s.strip() + ' - '
            weight = weight[0:-3].strip()

            data.append((name, due, weight))
        
        return data

    @botcmd(split_args_with=" ")
    def whatsdue(self, message, args):
        """
        Usage:  !whatsdue - Tries to read the current course channel for assessment
                !whatsdue [COURSE_CODE]... - List of course codes for finding assessment
        """
        courses = []

        # Fetch our courses from args/channel name depending on if args were supplied
        if len(args) == 1 and args[0] == '':
            try:
                courses.append(self.get_channel_name(message))
            except ValueError:
                return "Invalid room"
        else:
            for arg in args:
                courses.append(arg)

        # [[Assessments for courses[0]], [Assessments for courses[1] ...]]
        # c[0] = name, c[1] = due, c[2] = weight
        courseData = []
        for c in courses:
            try:
                courseData.append(self.get_assessment(c))
            except ValueError:
                # Send message that course was invalid
                return "Invalid course: " + c
        print(courseData)

        resultMessage = ("_*WARNING:* Assessment information may " +
                         "vary/change/be entirely different! Use " +
                         "at your own discretion_\r\n>>>")

        for i in range(0, len(courses)):
            for a in courseData[i]:
                resultMessage += ("*" + courses[i].upper() + "*: " +
                        "`" + a[0] + "` " +
                        "_(" + a[1] + ")_ " +
                        "*" + a[2] + "*" + "\r\n")

            event = message.extras.get('slack_event')
        # Api call to avoid markdown formatting issues
        self._bot.api_call('chat.postMessage', data = {
            'channel': message.extras.get('slack_event').get('channel'),
            'text': resultMessage,
            'as_user': 'true',
            })
