#!/usr/bin/python3
"""CLI for handling data input"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Comman line interface for user input"""

    prompt = "(hbnb) "

    def __init__(self):
        """Initalize the CLI"""
        super().__init__()

    def do_EOF(self, arg):
        """command to exit the program
        """
        return True

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    # def do_help(self, arg):
    #     """Show documented Commands"""
    #     pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
