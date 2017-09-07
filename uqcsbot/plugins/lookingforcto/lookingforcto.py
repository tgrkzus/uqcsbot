from errbot import BotPlugin, botcmd


class LookingForCTO(BotPlugin):

    @botcmd  # flags a command
    def lookingforcto(self, msg, args):  # a command callable with !tryme
        return "http://arcticstartup.com/article/no-i-wont-be-your-technical-co-founder/"
