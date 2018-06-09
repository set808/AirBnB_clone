#!/usr/bin/python3
"""Command line console for HBNB"""

import cmd
import readline
import models
User = models.user.User
BaseModel = models.user.BaseModel
storage = models.storage

def strtoargs(argstr):
    """convert a string to list of arguments"""
    return argstr.split()

class HBNBCommand(cmd.Cmd):
    """Command line console for HBNB. Use 'help' or '?' in console\
    for command documentation.
    """
    prompt = '(HBNB) '

    def do_create(self, arg):
        """Create an instance of a class.\
        Usage: create <classname>\
        """
        arg = strtoargs(arg)
        if len(arg) < 1:
            print("** class name missing **")
        elif arg[0] == "BaseModel":
            newmodel = BaseModel()
            print(newmodel.id)
            storage.new(newmodel)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Show an instance of a class.\
        Usage: show <classname> <uuid>\
        """
        arg = strtoargs(arg)
        if len(arg) < 1:
            print("** class name missing **")
        elif arg[0] in ["BaseModel"]:
            if len(arg) < 2:
                print("** instance id missing **")
            else:
                print(str(storage.get_object(arg[1])))
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Destroy a class instance by uuid.\
        Usage: destroy <classname> <uuid>\
        """
        arg = strtoargs(arg)
        if len(arg) < 1:
            print("** class name missing **")
        else:
            print(arg[0])
            if arg[0] in ["BaseModel"]:
                if len(arg) < 2:
                    print("** instance id missing **")
                else:
                    try:
                        del storage.all()[arg[0] + "." + arg[1]]
                    except KeyError:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """Print all instances of a class, or all instances with no args.\
        Usage: all [classname]\
        """
        arg = strtoargs(arg)
        objects = storage.all()
        if len(arg) < 1:
            print("[", end="")
            print(", ".join(str(objects[obj]) for obj in objects), end="]\n")
        else:
            if arg[0] in ["BaseModel"]:
                print("[", end="")
                print(", ".join(str(objects[obj])
                                for obj in objects
                                if objects[obj].__class__.__name__ == arg[0]),
                      end="]\n")
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance of a class based on uuid\
        Usage: update <classname> <uuid> <attribute> <value>\
        """
        arg = strtoargs(arg)
        if len(arg) < 1:
            print("** class name missing **")
        else:
            if arg[0] in ["BaseModel"]:
                if len(arg) >= 2:
                    obj = storage.get_object(arg[1])
                    if storage.get_object(arg[1]):
                        if len(arg) < 3:
                            print("** attribute name missing **")
                        elif len(arg) < 4:
                            print("** value missing **")
                        else:
                            """Might want to check invalid data type here"""
                            setattr(obj, arg[2], arg[3])
                    else:
                        print("** no instance found **")
                else:
                    print("**instance id missing **")
            else:
                print("** class doesn't exist **")

    def do_quit(self, arg):
        """Quit the shell"""
        return 1

    def do_EOF(self, arg):
        """Quit the shell"""
        return 1

    def emptyline(self):
        return 0

if __name__ == "__main__":
    HBNBCommand().cmdloop()
