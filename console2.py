#!/usr/bin/python3
"""
    Module contains the entry to command interpreter.
"""
import cmd
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = '(hbnb)'
    clas = {"BaseModel", "State", "City",
            "Amenity", "Place", "Review", "User"}

    def do_quit(self, *args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, *args):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """If this method is not overridden, repeats the last
            nonempty command entered"""

    def do_create(self, args):
        """Create instances"""
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args not in HBNBCommand.clas:
            print("** class doesn't exist **")
            return
        else:
            new_instance = eval(args)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, args):
        """Print string representation: name and id"""
        args = args.split()

        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            if args[0] not in HBNBCommand.clas:
                print("** class doesn't exist **")
            else:
                if len(args) == 1:
                    print("** instance id missing **")
        else:
            if args[0] not in HBNBCommand.clas:
                print("** class doesn't exist **")
            else:
                idcheck = args[0] + "." + args[1]
                all_objects = models.storage.all()

                if idcheck not in all_objects:
                    print("** no instance found **")
                else:
                    print(all_objects[idcheck])

    def do_destroy(self, args):
        """Destroy instance specified by user; Save changes to JSON file"""
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            if args[0] not in HBNBCommand.clas:
                print("** class doesn't exist **")
            else:
                if len(args) == 1:
                    print("** instance id missing **")
        else:
            if args[0] not in HBNBCommand.clas:
                print("** class doesn't exist **")
            else:
                idcheck = args[0] + "." + args[1]
                all_objects = models.storage.all()

                if idcheck not in all_objects:
                    print("** no instance found **")
                else:
                    del all_objects[idcheck]
                    models.storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
