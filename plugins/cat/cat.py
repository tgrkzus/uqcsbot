from errbot import BotPlugin, botcmd


class Cat(BotPlugin):

    @botcmd  # flags a command
    def cat(self, msg, args):  # a command callable with !tryme
        """
        Prints a moss cat!
        """
        return r"""
        ```
                   __..--''``\\--....___   _..,_
               _.-'    .-/\";  `        ``<._  ``-+'~=.
           _.-' _..--.'_    \\                    `(^) )
          ((..-'    (< _     ;_..__               ; `'   fL
                     `-._,_)'      ``--...____..-'
        ```
        """

