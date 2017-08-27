from errbot import BotPlugin
from errcron import CrontabMixin
from errbot.backends.slack import SlackRoom
from random import choice

class Wakie(CrontabMixin, BotPlugin):
    CRONTAB = [
        '40 * * * * .try_it',
        '40 * * * * .try_it',
    ]
    
    def try_it(self, polled_time):
        user = self.build_identifier('#general')
        room = SlackRoom(name="general", bot=self._bot)
        occupants = room.occupants
        victim = choice(occupants).username
        return self.send(user, 'Hey @{}! Tell us about something cool you are working on!'.format(victim))
