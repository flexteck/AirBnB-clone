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
    classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
    }

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
        args = shlex.split(args)
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
        args = shlex.split(args)
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


    def do_update(self, arg):
        """ Updates an instance based on class name and id"""
        args = shlex.split(arg)

        if not args:
             print("** class name missing **")
             return
        
        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = f"args[0].args[1]"
        obj = storage.all().get(key)

        if key is None:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        attr_name = args[2]
        attr_value = args[3]

        if hasattr(obj, attr_name):
            attr_type = type(getattr(attr_name))
            try:
                attr_value = attr_type(attr_value)
            except ValueError:
                pass
        setattr(obj, attr_name, attr_value)
        obj.save()


    def default(self, line):
        " Handles command in the format `<class name>.nethod()` """
        args = line.split(".")

        if len(args) == 2:
            class_name, method_call = args

            if class_name not in self.classes:
                 print("** class does not exist **")
                 return

            if method_call == "all()":
                return self.do_all(class_name)

            elif method_call == "count()":
                count = sum(1 for key in storage.all().keys() if key.startswith(class_name))
                print(count)
                return

            elif method_call.startswith("show(") and method_call.endswith(")"):
                obj_id = method_call[5:-1]
                return self.do_show(f"{class_name} {obj_id}")

            elif method_call.startswith("destroy(") and method_call.endswith(")"):
                obj_id = method_call[8:-1]
                return self.do_show(f"{class_name} {obj_id}") 

            elif method_call.startswith("update(") and method_call.endswith(")"):
                args = shlex.split(method_call[7:-1])
                
                if len(args) == 2:
                    obj_id = args[0].strip()
                    obj_instance = args[1]

                    for key, value in eval(obj_instance).items():
                        arg = f"{class_name} {obj_id} {key} {value}"
                        self.do_update(arg)
                    return
                elif len(args) == 3:
                    obj_id, attr_name, attr_value = args[:3]
                    self.do_update(f"{class_name} {obj_id} {attr_name} {attr_value}")
                    return

            else:
                    print(f"*** Unknown syntax: {line}")
        else:
             print(f"*** Unknown syntax: {line}")



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
