from errbot import BotPlugin, botcmd


class Id(BotPlugin):
    @botcmd  # flags a command
    def id(self, msg, args):  # a command callable with !tryme
        self.send(msg.frm, msg.extras['slack_event']['user'])  # This string format is markdown.
