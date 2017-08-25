from errbot import BotPlugin, botcmd

BOT_IDENTITY = {
    'token': 'xoxb-232547880822-s0bPC5Swpuf2bDmVcIf59Z1Z',
}

BOT_ADMINS = ('@ndl', '@tgrkzus')

BOT_ALT_PREFIXES = ('@nickbot',)

CHATROOM_PRESENCE = ()

class HelloWorld(BotPlugin):
    
    @botcmd
    def hello(self, msg, args):
        return "Hello, world!";
