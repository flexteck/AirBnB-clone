#!/usr/bin/python3
import cmd, sys
import json
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


class   HBNBCommand(cmd.Cmd):
    """ Command interpreter for HBNB """
    prompt = '(hbnb) '
    classes = {"BaseModel": BaseModel, "User": User}

    # ---- basic command ----

    def do_create(self, arg):
        """Creates a new instance of BaseModel and save it """
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = self.classes[arg]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """ shows the string representation of an instance """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("instance id missing **")
            return
        if len(args) < 2:
            print("Instance id is missing")
            return
        key = f"{args[0]}.{args[1]}"
        objects = storage.all()
        if key not in objects:
            print("** no instance found ")
            return
        print(objects[key])


    def do_destroy(self, args):
        """ Delete an instance based on class name and id """
         args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("instance id missing **")
            return
        if len(args) < 2:
            print("Instance id is missing")
            return
        key = f"{args[0]}.{args[1]}"
        objects = storage.all()
        if key not in objects:
            print("** no instance found ")
            return
        del objects[key]
        storage.save()


    def do_all(self, arg):
        """ print all instance based on class name or all instance """
        objects = storage.all()

        if arg and arg not in self.classes:
            print("** class does not exist ** ")
            return
        result = [str(obj) for key, obj in objects.items() if not arg or key.startswith(arg)]
        print(result)


    def do_quit(self, line):
        """quit the shell"""
        return True

    def do_EOF(self, line):
        print()
        return True

    def emptyline(self):
        """overrides empty line behaviour to do nothing"""
        pass

if __name__ == '__main__':
    if sys.stdin.isatty():
        HBNBCommand().cmdloop()
    else:
        for line in sys.stdin:
            HBNBCommand().onecmd(line.strip())
