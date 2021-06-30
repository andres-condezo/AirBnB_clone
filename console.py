#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User

class HBNBCommand(cmd.Cmd):
    """The command interpreter class"""
    prompt = ('(hbnb) ')
    my_classes = ["BaseModel", "User"]

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
        key_for_search = "{}.{}".format(tokens[0], tokens[1])
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
