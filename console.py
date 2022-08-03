#!/usr/bin/env python3

"""
    A module for AirBnB console
"""

import cmd
import re
from models.base_model import BaseModel
from models import storage
import json

class HBNBCommand(cmd.Cmd):
    """A class for the command interpreter."""
    prompt = "(hbnb) "

    def default(self, line):
        """
            Method called on an input line when the command prefix is not recognized.\
            If this method is not overridden\
            it prints an error message and returns."""
        self.__precmd(line)

    def _precmd(self, line):
        """Executed just before the cmd line is interpreted\
         and after the input prompt is generated"""
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            return line
        classname = match.group(1)
        method = match.group(2)
        args = match.group(3)
        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_uid_and_args:
            uid = match_uid_and_args.group(1)
            attr_or_dict = match_uid_and_args.group(2)
        else:
            uid = args
            attr_or_dict = False

        attr_and_value = ""
        if method == "update" and attr_or_dict:
            match_dict = re.search('^({.*})$', attr_or_dict)
            if match_dict:
                self.update_dict(classname, uid, match_dict.group(1))
                return ""
            match_attr_and_value = re.search('^(?:"([^"]*)")?(?:, (.*))?$', 
                    attr_or_dict)
            if match_attr_and_value:
                attr_and_value = (match_attr_and_value.group(1) or ""
                                  + " " + (match_attr_and_value.group(2) or ""))
        command = method + " " + classname + " " + uid + " " + attr_and_value
        self.onecmd(command)
        return command
    

    def update_dict(self, classname, uid, s_dict):
        """
            a method to update the dict
        """
        s = s_dict.replace("'", '"')
        d = json.loads(s)
        if not classname:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            else:
                attributes = storage.attributes()[classname]
                for attribute, value in d.items():
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()
    
    def do_EOF(self, line):
        """Handles EOF char"""
        print()
        return True
    
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Doesnt do anything"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        if line == "" or line is None:
            print("** class name missing **")
        
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            new_instance = storage.classes()[line]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """prints the string representation of the obj"""
        if line is None or line == "":
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                name_id = "{}.{}".format(words[0], words[1])
                if name_id not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[name_id])
    
    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if line is None or line == "":
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                name_id =" {}.{}".format(name_id[0], name_id[1])
                if name_id not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[name_id]
                    storage.save()

    def do_all(self, line):
        """Prints all string representation of allinstances\
                based or not on the class name """
        if line != "":
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                st_r = [str(obj) for key, obj in storage.all().items()
                        if type(obj).__name__ == words[0]]
                print(st_r)
        else:
            st_r = [str(obj) for key, obj in storage.all().items()]
            print(st_r)

    def do_update(self, line):
        """Updates an instance based on the class name\
                and id by adding or updating attribute """
        if line == "" or line is None:
            print("** class name is missing **")
            return

        regx = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(regx, line)
        classname = match.group(1)
        uid = match.group(2)
        atr_name = match.group(3)
        atr_value = match.group(4)
        if not match:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            elif not atr_name:
                print("** attribute name missing **")
            elif not atr_value:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', atr_value):
                    if '.' in atr_value:
                        cast = float
                    else:
                        cat = int
                else:
                    atr_value = atr_value.replace('"', '')
                attributes = storage.attributes()[classname]
                if atr_name in attributes:
                    atr_value = attributes[atr_name](atr_value)
                elif cast:
                    try:
                        atr_value = cast(atr_value)
                    except ValueError:
                        pass
                setattr(storage.all()[key], atr_name, atr_value)
                storage.all()[key].save()



if __name__ == '__main__':
    HBNBCommand().cmdloop()
