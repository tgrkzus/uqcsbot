from errbot import BotPlugin, botcmd
from icalendar import Calendar, Event
import requests

class Events(BotPlugin):
    @botcmd  # flags a command
    def events(self, msg, args):
        res = requests.get("https://calendar.google.com/calendar/ical/q3n3pce86072n9knt3pt65fhio%40group.calendar.google.com/public/basic.ics")
        cal = Calendar.from_ical(res.text)
        events = ""
        for e in cal.walk('vevent'):
            events += str(e.get('summary')) + "\n"
        return events
