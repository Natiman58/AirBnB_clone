#!/usr/bin/env python3

"""
    A module for AirBnB console
"""

import cmd
import re



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



if __name__ == '__main__':
    HBNBCommand().cmdloop()
