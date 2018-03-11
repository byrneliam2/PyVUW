"""
Liam Byrne (byrneliam2)
PyVUW
"""

import user.io


class UI:

    # Execution
    running = True

    def __init__(self, org):
        self._org = org
        self.print_all()

    # ------------------------------------------------------------------------------

    def do_next(self):
        """
        Take a user input and perform the operation it translates to, if it is correct.
        """

        def arg_check(num):
            """
            Inner function to check for proper number of arguments.
            :param num: number of expected trailing arguments (after the command itself)
            """
            if len(args[1:]) < num:
                print("error: need more arguments")
                return True
            return False

        # get the input and split into a list of arguments
        args = input("> ").split()

        # no input, no response
        if len(args) == 0:
            return

        # commands with arguments
        if args[0] == "a":
            if arg_check(1):
                return
            self._org.add_data(args[1], args[2:])
        elif args[0] == "del":
            if arg_check(1):
                return
            self._org.del_data(args[1], args[2:])
        elif args[0] == "e":
            if arg_check(3):
                return
            self._org.edit_data(args[1], args[2], args[3])
        elif args[0] == "man":
            # print(user.io.OutputHandler.write_man())
            self.print_man(args[1] if len(args) == 2 else None)

        # no argument commands
        elif args[0] == "s":
            user.io.OutputHandler.write_out(self._org)
        elif args[0] == "v":
            self.print_all()
        elif args[0] == "x":
            self.running = False
        elif args[0] == "xf":
            exit()

        else:
            # it must be an invalid command
            self.print_invalid(args[0])

    def print_man(self, cmd):
        """
        Print the manual. If no command is present, then the full list of manuals available
        is printed out. Otherwise, that specific manual is printed.
        :param cmd: command to look up manual for
        """
        mans = user.io.OutputHandler.list_mans()
        if cmd is None:
            # None type passed in indicates no command to look up
            # could use list slicing, but we are only looking for one argument so manipulating
            # a list probably isn't worth it
            print("Current commands: ")
            print(mans)
            print("\nType \"man [cmd]\" to learn more about the command.")
        elif cmd not in mans:
            # there must be a command, but is it valid? use the mans list we have created already
            # to check
            self.print_invalid(cmd)
        else:
            # look up and print the manual
            print(user.io.OutputHandler.print_man(cmd))

    @staticmethod
    def print_invalid(cmd):
        """
        Alert the user that the command they have entered is not valid.
        :param cmd: invalid command
        """
        print("error: command " + cmd + " is not valid")

    def print_all(self):
        """
        Reprint the entire organiser.
        """

        t_name = 10

        print("=" * t_name + " PyVUW Organiser " + "=" * t_name)
        print()
        print("Type \"man\" for help.")
        print("(" + str(len(self._org)) + " courses, " + str(self._org.total_work()) + " tasks)")
        print()
        for course, tasks in self._org:
            print(course + ": ", end='')
            for t in tasks:
                print(t + " ", end='')
            print()
            print("-" * len(course), end='')
            print("-" * (sum(len(t) for t in tasks) + len(tasks) + 1))

            # note that the above line essentially prints a series of hyphens the exact same length
            # of the line printed above it, this is to separate the courses and to provide a visual
            # indication of the number of tasks for that course.
            # what if the course names all have different lengths? won't this look weird then?
            # typically in a university setting, courses will all have some naming convention (such
            # as SWEN222) where the course codes are the same length, therefore we rely on this
            # assumption.
