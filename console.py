#!/usr/bin/python3
import cmd, sys

class AirBnB(cmd.Cmd):
    prompt = '(hbnb) '

    # ---- basic command ----

    def do_quit(self, line):
        """quit the shell"""

    def do_EOF(self, line):
        print()
        return True

if __name__ == '__main__':
    if sys.stdin.isatty():
        AirBnB().cmdloop()
    else:
        for line in sys.stdin:
            AirBnB().onecmd(line.strip())
