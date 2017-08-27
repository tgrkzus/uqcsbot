from errbot import BotPlugin, botcmd


class Welcome(BotPlugin):
    def callback_message(self, message):
        welcomeMessages = [
            "Hey there! Welcome to the UQCS slack!",
            "This is the first time I've seen you, so you're probably new here",
            "I'm UQCSbot, your friendly (open source) robot helper",
            "We've got a bunch of generic channels (e.g. #banter, #games, #projects) along with many subject-specific ones",
            "Your friendly admins are @trm, @dmarj97, @cat, @gricey, @csa, @ainz, and @mqt",
            "Type \"!help\" here, or \"!uqcsbot help\" anywhere else to find out what I can do.",
            "And again, welcome :)"
        ]
        
        channel_code = message.extras['slack_event']['channel']
        channel_name = self._bot.channelid_to_channelname(channel_code)
        channel_id = self.build_identifier('#'+channel_name)
        subtype = message.extras.get('slack_event').get('subtype')
        if subtype != None:
            if subtype == 'channel_join' and channel_name == 'random':
                user = self._bot.userid_to_username(message.extras['slack_event']['user'])
                self.send(channel_id, 'Welcome ' + user)
            for msg in welcomeMessages: 
                self.send(message.frm, msg)
