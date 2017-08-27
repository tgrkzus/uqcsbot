from errbot import BotPlugin, botcmd, arg_botcmd, webhook

"""
No worky
"""

class ModeratedChannel():
    def __init__(self, channel, mods):
        # Channel id (not name)
        self.channel = channel
        # List of mod user ids 
        self.mods = mods

class Moderate(BotPlugin):
    #SLACK_ADMIN_TOKEN = os.environ["SLACK_ADMIN_TOKEN"] 

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
        event = message.extras.get('slack_event')
        print(message)
        #if (event.
        #        if (self._bot.userid_to_username(event.get('user')) == perpetrator):
        #        self.manual_chat_delete(self.SLACK_ADMIN_TOKEN, event.get('channel'), event.get('ts'))
