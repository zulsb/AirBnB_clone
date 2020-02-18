#!/usr/bin/python3
"""
    Module contains the entry to command interpreter.
"""
import cmd
from models.base_model import BaseModel
import json
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
import shlex


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""

    classes = {
            "BaseModel": BaseModel, "User": User,
            "Amenity": Amenity, "City": City, "State": State,
            "Place": Place, "Review": Review
            }

    file_path = "file.json"
    prompt = '(hbnb)'

    ins = []

    def do_quit(self, *args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, *args):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """If this method is not overridden, repeats the last
            nonempty command entered"""
        pass

    def do_create(self, arg):
        """Create new instance of class"""
        args = arg.split(" ")
        if len(args[0]) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            b = self.classes[args[0]]()
            print(b.id)
            self.ins.append(b)
            b.save()

    def do_show(self, arg):
        """Method to show Class Instance by ID #"""
        args = arg.split(" ")
        if len(args[0]) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            idn = "[{}] ({})".format(args[0], args[1])
            flag = 0
            for ins in self.ins:
                if idn in ins.__str__():
                    print(ins)
                    flag = 1
            if flag == 0:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Method to destroy instance of class via ID number"""
        args = arg.split(" ")
        flag = 0
        if len(args[0]) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            idn = "[{}] ({})".format(args[0], args[1])
            for ins in self.ins:
                if idn in ins.__str__():
                    self.ins.remove(ins)
                    flag = 1

            if flag == 0:
                print("** no instance found **")
            else:
                with open(HBNBCommand.file_path, "r") as f:
                    jobj = json.load(f)

                del jobj["{}.{}".format(args[0], args[1])]

                with open(HBNBCommand.file_path, "w") as f:
                    json.dump(jobj, f)

    def do_all(self, arg):
        """Method to show all instances"""
        args = arg.split(" ")
        if len(args[0]) == 0:
            print([x.__str__() for x in self.ins])
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            print([x.__str__() for x in self.ins if args[0] in x.__str__()])

    def do_update(self, arg):
        """Method to update instance"""
        if arg == "":
            print("** class name missing **")
            return
        args = shlex.split(arg)
        if args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            flag = 0
            idn = "[{}] ({})".format(args[0], args[1])
            for ins in self.ins:
                if idn in ins.__str__():
                    flag = 1
            if flag == 0:
                print("** no instance found **")
                return
            elif len(args) == 2:
                print("** attribute name missing **")
                return
            elif len(args) == 3:
                print("** value missing **")
                return
            else:
                idn = "[{}] ({})".format(args[0], args[1])
                for ins in self.ins:
                    if idn in ins.__str__():
                        try:
                            val = int(args[3])
                        except ValueError:
                            try:
                                val = float(args[3])
                            except ValueError:
                                val = args[3]

                        setattr(ins, args[2], val)
                        ins.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
