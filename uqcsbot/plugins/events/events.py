from errbot import BotPlugin, botcmd
from icalendar import Calendar, Event
import datetime
import requests

class Events(BotPlugin):
    @staticmethod
    def getEvents(cal, weeks):
        """
        Get's the events in the next weeks
        """
        events = []
        margin = datetime.timedelta(days = (7 * weeks))
        for e in cal.walk('vevent'):
            start = e.get('DTSTART')
            # Get now date relative to timezone of event
            now = datetime.datetime.now(start.dt.tzinfo)
            # If event started within margin (or within the last day)
            if (now - datetime.timedelta(days = 1) <= start.dt <= now + margin):
                events.append(e)
        return events

    @botcmd  # flags a command
    def events(self, msg, args):
        """
        Prints events in the near future
        """

        # Get cal object from google
        res = requests.get("https://calendar.google.com/calendar/ical/q3n3pce86072n9knt3pt65fhio%40group.calendar.google.com/public/basic.ics")
        cal = Calendar.from_ical(res.text)

        dateFormat = "%b %d %H:%M"
        weeks = 0
        full = False
        events = []
        eventStr = ""

        # Check arg 1 (weeks/full)
        arguments = args.split(" ")
        if len(arguments) == 1 and arguments[0] == '':
            weeks = 2
        elif arguments[0] == "full":
            full = True
        else:
            try:
                weeks = int(arguments[0])
            except ValueError:
                return "Invalid parameters"

        # Process full/weeks
        if full:
            # Let's say there's not gonna be events planned ahead more than a year
            events = self.getEvents(cal, 52)
            eventStr = "All upcoming events:\n"
        else:
            events = self.getEvents(cal, weeks)
            eventStr = "Events in the **next " + str(weeks) + " weeks:**\n\n"
        
        # Iterate through our chosen events and format them
        for e in events:
            summary = str(e.get('SUMMARY'))
            start = e.get('DTSTART').dt
            end = e.get('DTEND').dt
            location = e.get('LOCATION')
            
            if (location == ""):
                location = "TBA"

            # This is sorta messy (note it's markdown formatting not slack!)
            eventStr += ("**" + str(start.strftime(dateFormat))
                    + " - "
                    + str(start.strftime(dateFormat)) + "**"
                    + " - "
                    + "*" + location + "*"
                    + ": "
                    + "`"
                    + summary
                    + "`\n\n")
        return eventStr

