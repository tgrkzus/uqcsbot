from errbot import BotPlugin, botcmd


class Example(BotPlugin):

    @botcmd  # flags a command
    def tryme(self, msg, args):  # a command callable with !tryme
        return 'It *works* !'  # This string format is markdown.
