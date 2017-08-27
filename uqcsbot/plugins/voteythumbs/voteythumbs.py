from errbot import BotPlugin, botcmd


class Voteythumbs(BotPlugin):

    @botcmd
    def voteythumbs(self, msg, args):
        self._bot.add_reaction(msg, "thumbsup")
        self._bot.add_reaction(msg, "thumbsdown")

