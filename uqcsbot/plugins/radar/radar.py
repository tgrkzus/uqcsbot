from errbot import BotPlugin, botcmd
import time
timestamp = str(time.time())

class Radar(BotPlugin):
    @botcmd  # flags a command
    def radar(self, msg, args):  # a command callable with !tryme
        return 'https://bom.lambda.tools/?location=brisbane&_cache=' + timestamp  # This string format is markdown.
