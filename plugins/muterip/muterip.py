from errbot import BotPlugin, botcmd
import os
import requests


class Muterip(BotPlugin):
    muted = False;
    SLACK_ADMIN_TOKEN = os.environ["SLACK_ADMIN_TOKEN"] 

    def manual_chat_delete(self, token, channel, ts):
        """
        slackclient doesn't allow custom tokens
        uses the env variable every time :(
        """
        prefix = "https://slack.com/api/chat.delete?"
        tokenC = "token=" + token + "&"
        channelC = "channel=" + channel + "&"
        tsC = "ts=" + ts

        requests.get(prefix + tokenC + channelC + tsC)

    def callback_message(self, message):
        if (self.muted):
            event = message.extras.get('slack_event')
            perpetrator = 'rip'
            if (self._bot.userid_to_username(event.get('user')) == perpetrator):
                self.manual_chat_delete(self.SLACK_ADMIN_TOKEN, event.get('channel'), event.get('ts'))


    @botcmd
    def muterip(self, message, args):
        """:rip: Rip Rip :rip:"""
        self.muted = not self.muted

