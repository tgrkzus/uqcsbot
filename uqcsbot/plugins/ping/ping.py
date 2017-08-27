from errbot import BotPlugin, botcmd, arg_botcmd, webhook


class Ping(BotPlugin):
    # Passing split_args_with=None will cause arguments to be split on any kind
    # of whitespace, just like Python's split() does
    @botcmd(split_args_with=None)
    def committee(self, message, args):
        """ Pings the committee """
        return "Committee: @trm, @dmarj97, @cat, @gricey, @csa, @ainz, @mqt"
