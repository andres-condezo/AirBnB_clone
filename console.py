#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User
from models.place import Place
from models.review import Review
from models.city import City
from models.state import State
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    """The command interpreter class"""
    prompt = ('(hbnb) ')
    my_classes = ["BaseModel", "User", "Place",
                  "Review", "State", "City", "Amenity"]

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

    def do_create(self, arg):
        """Creates a new instance of  a class model"""
        if not arg:
            print("** class name missing **")
        elif arg not in self.my_classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        tokens = arg.split()
        if not arg:
            print("** class name missing **")
        elif tokens[0] not in self.my_classes:
            print("** class doesn't exist **")
        elif len(tokens) < 2:
            print("** instance id missing **")
        else:
            key_for_search = "{}.{}".format(tokens[0], tokens[1])
            all_objects = storage.all()

            if key_for_search in all_objects.keys():
                print(all_objects[key_for_search])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        tokens = arg.split()
        if not arg:
            print("** class name missing **")
        elif tokens[0] not in self.my_classes:
            print("** class doesn't exist **")
        elif len(tokens) < 2:
            print("** instance id missing **")
        else:
            key_for_search = "{}.{}".format(tokens[0], tokens[1])
            all_objects = storage.all()

            if key_for_search in all_objects.keys():
                del all_objects[key_for_search]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances
            based or not on the class name"""
        tokens = arg.split()
        all_list = []
        all_objects = storage.all()

        if len(tokens) < 1:
            for value in all_objects.values():
                all_list.append(str(value))
            print(all_list)
        elif tokens[0] in self.my_classes:
            class_for_search = tokens[0]
            for key, value in all_objects.items():
                if class_for_search in key:
                    all_list.append(str(value))
            print(all_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        tokens = arg.split()
        all_objects = storage.all()

        if len(tokens) == 0:
            print("** class name missing **")
        elif tokens[0] not in self.my_classes:
            print("** class doesn't exist **")
        elif len(tokens) == 1:
            print("** instance id missing **")
        elif len(tokens) == 2:
            print("** attribute name missing **")
        elif len(tokens) == 3:
            print("** value missing **")
        else:
            key_for_search = "{}.{}".format(tokens[0], tokens[1])
            if key_for_search in all_objects:
                my_object = all_objects[key_for_search]

                tokens2 = tokens[2].replace('"', '')
                tokens3 = eval(tokens[3])

                if hasattr(my_object, tokens2):
                    new_type = type(getattr(my_object, tokens2))
                    tokens3 = new_type(tokens3)

                setattr(my_object, tokens2, tokens3)

                storage.save()
            else:
                print("** no instance found **")

    def do_count(self, arg):
        """Retriieve the number of instances of a class"""
        all_list = []
        all_objects = storage.all()

        if arg in self.my_classes:
            class_for_search = arg
            for key, value in all_objects.items():
                if class_for_search in key:
                    all_list.append(str(value))
        print(len(all_list))

    def default(self, arg):
        """Method called on an input line when the command prefix
        is not recognized"""
        # my_functions = {"all()": "do_all", "show": "do_show"}

        if '.' in arg:
            tokens = arg.split(".")

            # if tokens[1] in my_functions:
            if tokens[1] == 'all()':
                print("Fun encontrada")
                self.do_all(tokens[0])
            elif tokens[1] == 'count()':
                self.do_count(tokens[0])
            # elif tokens[1] == 'show()'
            else:
                messg = "** Unknown syntax: " + arg
                print(messg)

        else:
            # print("no tiene puntos")
            messg = "** Unknown syntax: " + arg
            print(messg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
