#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """The command interpreter class"""
    prompt = ('(hbnb) ')

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Handles End Of File character"""
        print()
        return True

    def emptyline(self):
        """Doesn't execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
