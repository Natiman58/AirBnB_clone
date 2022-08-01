#!/usr/bin/env python3

"""
    A module for AirBnB console
"""

import cmd


class ABConsole(cmd.Cmd):
    """A class for the command interpreter."""
    prompt = "(hbnb) "

    def default(self, line):
        """"""


if __name__ == '__main__':
    ABConsole().cmdloop()