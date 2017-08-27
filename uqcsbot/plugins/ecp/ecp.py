from errbot import BotPlugin, botcmd
import requests
from bs4 import BeautifulSoup

class Ecp(BotPlugin):

    @botcmd(split_args_with=" ")
    def ecp(self, msg, args):
        """
        Finds the ecp for the current course or... TODO
        """
        result = ""
        response = requests.get("https://www.uq.edu.au/study/course.html?course_code=" + args[0])

        if (response.status_code != 200):
            return "Error getting course profile"

        soup = BeautifulSoup(response.text, 'html.parser')

        if (soup.find("course-notfound") != None):
            return "Course not found"

        

        print(soup.prettify())
        return result
