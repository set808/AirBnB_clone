#!/usr/bin/python3
"""Command line console for HBNB"""

import shlex
import json
import cmd
import readline
import models
BaseModel = models.user.BaseModel
User = models.user.User
Place = models.place.Place
State = models.state.State
Amenity = models.amenity.Amenity
Review = models.review.Review
City = models.city.City
storage = models.storage

class HBNBCommand(cmd.Cmd):
    """Command line console for HBNB. Use 'help' or '?' in console\
    for command documentation.
    """
    prompt = '(HBNB) '
    __validclasses = ["BaseModel", "User", "Place", "Amenity", "Review",
                      "City", "State"]

    def do_create(self, arg):
        """Create an instance of a class.\
        Usage: create <classname>\
        """
        arg = shlex.split(arg)
        if len(arg) < 1:
            print("** class name missing **")
        elif arg[0] == "BaseModel":
            newmodel = BaseModel()
            print(newmodel.id)
            storage.new(newmodel)
        elif arg[0] == "User":
            newmodel = User()
            print(newmodel.id)
            storage.new(newmodel)
        elif arg[0] == "Place":
            newmodel = Place()
            print(newmodel.id)
            storage.new(newmodel)
        elif arg[0] == "Amenity":
            newmodel = Amenity()
            print(newmodel.id)
            storage.new(newmodel)
        elif arg[0] == "Review":
            newmodel = Review()
            print(newmodel.id)
            storage.new(newmodel)
        elif arg[0] == "City":
            newmodel = City()
            print(newmodel.id)
            storage.new(newmodel)
        elif arg[0] == "State":
            newmodel = State()
            print(newmodel.id)
            storage.new(newmodel)
        else:
            print("** class doesn't exist **")
            return
        storage.save()

    def do_show(self, arg):
        """Show an instance of a class.\
        Usage: show <classname> <uuid>\
        """
        arg = shlex.split(arg)
        if len(arg) < 1:
            print("** class name missing **")
        elif arg[0] in self.__validclasses:
            if len(arg) < 2:
                print("** instance id missing **")
            else:
                obj = storage.get_object(arg[1])
                if obj is None:
                    print("** no instance found **")
                else:
                    print(str(obj))
        else:
            print("** class doesn't exist **")
            return

    def do_destroy(self, arg):
        """Destroy a class instance by uuid.\
        Usage: destroy <classname> <uuid>\
        """
        arg = shlex.split(arg)
        if len(arg) < 1:
            print("** class name missing **")
        else:
            print(arg[0])
            if arg[0] in self.__validclasses:
                if len(arg) < 2:
                    print("** instance id missing **")
                else:
                    try:
                        del storage.all()[arg[0] + "." + arg[1]]
                        storage.save()
                    except KeyError:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """Print all instances of a class, or all instances with no args.\
        Usage: all [classname]\
        """
        arg = shlex.split(arg)
        objects = storage.all()
        if len(arg) < 1:
            print("[", end="")
            print(", ".join(str(objects[obj]) for obj in objects), end="]\n")
        else:
            if arg[0] in self.__validclasses:
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
        print(arg)
        arg = shlex.split(arg)
        if len(arg) < 1:
            print("** class name missing **")
        else:
            if arg[0] in self.__validclasses:
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
                            storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("**instance id missing **")
            else:
                print("** class doesn't exist **")

    def _do_count(self, arg):
        """prints the number of a type of instance in storage.
        Usage: count <classname>
        """
        shlex.split(arg)
        arg = strtoargs(arg)
        if len(arg) < 1:
            print("** class name missing **")
            return
        count = 0
        objects = storage.all()
        for key in objects:
            if objects[key].__class__.__name__ == arg[0]:
                count += 1
        print(count)
        
    def default(self, line):
        """Parse function style syntax for some commands. Regular error
        message otherwise.
        """
        classname = line.split(".", 1)
        if len(classname) < 2:
            print("** Unknown syntax:", line)
            return
        if classname[0] not in self.__validclasses:
            print("** class doesn't exist **")
            return
        methodname = classname[1].split("(", 1)
        if methodname[0] not in ["count", "all", "show", "destroy", "update"]\
           or len(methodname) < 2:
            print("** Unknown syntax:", line)
            return
        methodname[1] = methodname[1].strip()
        if len(methodname[1]) < 1 or methodname[1][-1] != ')':
            print("** Unknown syntax:", line)
            return
        args = methodname[1][:-1]
        if methodname[0] == "show":
            return self.do_show(classname[0] + " " + args)
        if methodname[0] == "all":
            return self.do_all(classname[0])
        if methodname[0] == "destroy":
            return self.do_destroy(classname[0] + " " + args)
        if methodname[0] == "count":
            return self._do_count(classname[0] + " " + args)
        if methodname[0] == "update":
            print(args)
            if len(args) < 1:
                print("** id not found **")
                return
            attrchk = args.split(",", 1)
            if len(attrchk) < 2:
                print("** attribute not found **")
                return
            print(attrchk)
            if attrchk[1].strip()[0] == "{":
                print(args)
                return self.update_dict(args)
            else:
                args = args.split(",", 2)
                return self.do_update(" ".join([classname[0]] + args))

    def update_dict(self, args):
        """Loads dictionary from args string then updates instance.
        Input args should be id then dict
        """
        args = args.split(",", 1)
        try:
            dicty = json.loads(args[1])
            print(dicty)
            print(type(dicty))
            if type(dicty) is not dict:
                print("** bad dictionary **")
        except json.decoder.JSONDecodeError:
            print("** bad dictionary **")
            return
        else:
            obj = storage.get_object(args[0])
            print(obj)
            if obj is None:
                print ("** id not found **")
                return
            for attr in dicty:
                exec("obj." + attr + " = dicty[attr]")

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
