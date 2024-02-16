#!/usr/bin/python3
"""CLI for handling data input"""

import sys
import cmd
import models
from models.base_model import BaseModel
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Comman line interface for user input"""

    prompt = "(hbnb) "
    __mods = {'BaseModel',
              "User"}

    def emptyline(self):
        """do nothing on empty line
        """
        pass

    def do_EOF(self, arg):
        """command to exit the program
        """
        print("")
        return True

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_create(self, arg):
        """Create a new model asn saves to Json file"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__mods:
            print("** class doesn't exist **")
        else:
            print(eval(args[0])().id)
            storage.save()

    def do_show(self, arg):
        """Show command to show specific instance"""
        args = arg.split()
        obj_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.__mods:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif "{}.{}".format(args[0], args[1]) not in obj_dict:
            print("** no instance found **")
            return
        else:
            print(obj_dict["{}.{}".format(args[0], args[1])])
            return

    def do_all(self, arg):
        """prints all the objects string rep"""
        args = arg.split()
        if len(args) > 0 and args[0] not in HBNBCommand.__mods:
            print("** class doesn't exist **")
            return
        else:
            objs = []
            for obj in storage.all().values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    objs.append(obj.__str__())
                elif len(args) == 0:
                    objs.append(obj.__str__())
            print(objs)

    def do_destroy(self, arg):
        """Destroy command to delete specific instance"""
        args = arg.split()
        obj_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__mods:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in obj_dict:
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        args = arg.split()
        obj_dict = storage.all()
        if len(args) == 0:
            print(" class name missing ")
            return False
        if args[0] not in HBNBCommand.__mods:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(args[0], args[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(args) == 2:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(args) == 4:
            objs = obj_dict["{}.{}".format(args[0], args[1])]
            if args[2] in objs.__class__.__dict__.keys():
                valty = type(objs.__class__.__dict__[args[2]])
                objs.__dict__[args[2]] = valty(args[3])
            else:
                objs.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            objs = obj_dict["{}.{}".format(args[0], args[1])]
            for k, v in eval(args[2]).items():
                if (k in objs.__class__.__dict__.keys() and
                        type(objs.__class__.__dict__[k]) in {str, int, float}):
                    valty = type(objs.__class__.__dict__[k])
                    objs.__class__.__dict__[k] = valty[v]
                else:
                    objs.__class__.__dict__[k] = v
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

    # if not sys.stdin.isatty():
    #     '''method is used to interpret the input as a comand'''
    #     for line in sys.stdin:
    #         '''Read command line by line'''

    #         HBNBCommand().onecmd(line.strip())
    #         '''method to remove whitespace from beg end'''
    # else:
    #     HBNBCommand().cmdloop()
