from errbot import BotPlugin, botcmd


class Spider(BotPlugin):

    @botcmd  # flags a command
    def spider(self, msg, args):  # a command callable with !tryme
        """
        Prints a moss cat!
        """
        return r"//\; ;/\\\\"

