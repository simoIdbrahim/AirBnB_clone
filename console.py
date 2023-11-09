#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ defines the HolbertonBnB command """

    prompt = '(hbnb)'
    validate_classes = ['BaseModel']

    def emptyline(self):
        """ do nothing """
        pass

    def do_quit(self, val):
        """ return True to exit the program """

        return True

    def do_help(self, val):
        """ this action is provided by default by cmd """

        print('Quit command to exit the program')

    def do_EOF(self, val):
        """ return True to exit the program """

        print()
        return True

    def do_create(self, val):
        """ creates a new instance of BaseModel """

        the_commend = shlex.split(val)

        if len(the_commend) == 0:
            print('** class name missing **')
        elif the_commend[0] not in self.validate_classes:
            print("** class doesn't exist **")
        else:
            new_user = BaseModel()
            new_user.save()
            print(new_user.id)

    def do_show(self, val):
        """
        prints the string representation of an
        instance based on the class name and id
        """
        the_commend = shlex.split(val)

        if len(the_commend) == 0:
            print('** class name missing **')
        elif the_commend[0] not in self.validate_classes:
            print("** class doesn't exist **")
        elif len(the_commend) < 2:
            print('** instance id missing **')
        else:
            objs = storage.all()

            key = '{}.{}'.format(the_commend[0], the_commend[1])
            if key in objs:
                print(objs[key])
            else:
                print('** no instance found **')

    def do_destroy(self, val):
        """
        deletes an instance based on the class name and
        id and save the change in json file.
        """
        the_commend = shlex.split(val)

        if len(the_commend) == 0:
            print('** class name missing **')
        elif the_commend[0] not in self.validate_classes:
            print("** class doesn't exist **")
        elif len(the_commend) < 2:
            print('** instance id missing **')
        else:
            objs = storage.all()

            key = '{}.{}'.format(the_commend[0], the_commend[1])
            if key in objs:
                del objs[key]
                storage.save()
            else:
                print('** no instance found **')

    def do_all(self, val):
        """
        displays all str representation of all instances
        based or not on the class name
        """
        objs = storage.all()

        the_commend = shlex.split(val)

        if len(the_commend) == 0:
            for k, v in objs.items():
                print(str(v))
        elif the_commend[0] not in self.validate_classes:
            print("** class doesn't exist **")
        else:
            for k, v in objs.items():
                if k.split('.')[0] == the_commend[0]:
                    print(str(v))

    def update(self, val):
        """
        updates an instance based on the class name and
        id by adding or updating attribute and save the
        change in jsin file.
        """
        the_commend = shlex.split(val)

        if len(the_commend) == 0:
            print('** class name missing **')
        elif the_commend[0] not in self.validate_classes:
            print("** class doesn't exist **")
        elif len(the_commend) < 2:
            print('** instance id missing **')
        else:
            objs = storage.all()

            key = '{}.{}'.format(the_commend[0], the_commend[1])

            if key not in objs:
                print('** no instance found **')
            elif len(the_commend) < 3:
                print('** attribute name missing **')
            elif len(the_commend) < 4:
                print('** value missing **')
            else:
                obj = objs[key]

                name = the_commend[2]
                value = the_commend[3]

                try:
                    value = eval(value)
                except Exception:
                    pass

                setattr(obj, name, value)

                obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
