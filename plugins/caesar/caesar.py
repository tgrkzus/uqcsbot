from errbot import BotPlugin, botcmd


class Example(BotPlugin):

    @botcmd(split_args_with=" ")  # flags a command
    def caesar(self, msg, args):  # a command callable with !caesar
        if len(args) > 1 and args[0].isdigit():
            key = int(args[0])
            text = ""
            shifted = ""
            for arg in args[1:]:
                text += arg + " "
            for char in text:
                if char.isalpha():
                    if ord('a') <= ord(char)  <= ord('z'):
                        shifted += chr((ord(char)-ord('a') + key%26) + ord('a'))
                    elif ord('A') <= ord(char) <= ord('Z'):
                        shifted += chr((ord(char)-ord('A') + key%26) + ord('A'))
                else:
                    shifted += char
            return shifted
        else:
            return 'Usage: !caesar [int] [text]'+str(len(args))

