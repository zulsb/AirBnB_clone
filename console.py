#!/usr/bin/python3
"""
    Module contains the entry to command interpreter.
"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = '(hbnb)'

    def do_quit(self, *args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, *args):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """If this method is not overridden, repeats the last
            nonempty command entered"""

if __name__ == '__main__':
    HBNBCommand().cmdloop()
