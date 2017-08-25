from errbot import BotPlugin, botcmd
from icalendar import Calendar, Event
import requests

class Events(BotPlugin):
    @botcmd  # flags a command
    def events(self, msg, args):
        cal = requests.get("https://calendar.google.com/calendar/ical/q3n3pce86072n9knt3pt65fhio%40group.calendar.google.com/public/basic.ics")
        return cal.text

