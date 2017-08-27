from errbot import BotPlugin, botcmd
import os
import requests


class Muterip(BotPlugin):
    muted = False
    funmuted = False
    perpetrator = 'rip'
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

    def manual_kick(self, token, channel, user):
        prefix = "https://slack.com/api/channels.kick?"
        tokenC = "token=" + token + "&"
        channelC = "channel=" + channel + "&"
        userC = "user=" + user

        requests.get(prefix + tokenC + channelC + userC)

    def callback_message(self, message):
        if (self.muted):
            event = message.extras.get('slack_event')
            if (self._bot.userid_to_username(event.get('user')) == self.perpetrator):
                self.manual_chat_delete(self.SLACK_ADMIN_TOKEN, event.get('channel'), event.get('ts'))
        if (self.funmuted):
            event = message.extras.get('slack_event')
            if (self._bot.userid_to_username(event.get('user')) == self.perpetrator):
                if event.get('subtype') != 'channel_join':
                    self.manual_kick(self.SLACK_ADMIN_TOKEN, event.get('channel'), event.get('user'))



    @botcmd(split_args_with=" ")  # flags a command
    def muterip(self, message, args):
        """:rip: Rip Rip :rip:"""
        if (args[0] == "fun"):
            self.muteripfun(message, args)
        else:
            self.muted = not self.muted

    def muteripfun(self, message, args):
        self.funmuted = not self.funmuted

    @botcmd
    def excommunicaterip(self, message, args):
        """:rip: fun rip rip :rip:"""
        channels = self._bot.rooms()

        for c in channels:
            if c.private:
                continue

            members = c.occupants

            for m in members:
                if m.username == self.perpetrator:
                    self.manual_kick(self.SLACK_ADMIN_TOKEN, c.id, m.userid) 

    @botcmd
    def surpriserip(self, message, args):
        """:rip: fun rip rip :rip:"""
        channels = self._bot.rooms()

        for c in channels:
            prefix = "https://slack.com/api/channels.invite?"
            tokenC = "token=" + self.SLACK_ADMIN_TOKEN + "&"
            channelC = "channel=" + c.id + "&"
            userC = "user=" + self._bot.username_to_userid(self.perpetrator)

            requests.get(prefix + tokenC + channelC + userC)


