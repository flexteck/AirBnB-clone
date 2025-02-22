#!/usr/bin/python3
import cmd, sys

class   HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    file = None

    # ---- basic command ----

    def do_quit(self, line):
        """quit the shell"""
        return True

    def do_EOF(self, line):
        print()
        return True

    def emptyline(self):
        """overrides empty line behaviour to do nothing"""
        pass

if __name__ == '__main__':
    if sys.stdin.isatty():
        HBNBCommand().cmdloop()
    else:
        for line in sys.stdin:
            HBNBCommand().onecmd(line.strip())
