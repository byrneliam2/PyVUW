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
                raise ImproperFormatException("need more arguments")

        # get the input and split into a list of arguments
        args = input("> ").split()

        try:
            # no input, no response
            if len(args) == 0:
                raise ImproperFormatException("no command found")

            # commands with arguments
            if args[0] == "a":
                arg_check(1)
                self._org.add_data(args[1], args[2:])
            elif args[0] == "del":
                arg_check(1)
                self._org.del_data(args[1], args[2:])
            elif args[0] == "e":
                arg_check(3)
                self._org.edit_data(args[1], args[2], args[3])  # ignore anything else after arg 3
            elif args[0] == "man":
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
                raise ImproperFormatException(args[0] + " is not a valid command")

        except ImproperFormatException as e:
            self.print_error(str(e))

    @staticmethod
    def format_tasks(tasks):
        """
        Take a list of tasks and return a new one that is properly formatted such that
        any elements surrounded by quotes are combined into a single task.
        """
        output = []
        current = ""
        for t in tasks:
            if t.startswith("\"") and not (t.endswith("\"")):
                current += t.replace("\"", "")
                while not t.endswith("\""):
                    current += t
                    continue
            else:
                if t.endswith("\""):
                    t = t.replace("\"", "")
                current += t
                output.append(current)
        return output

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
            self.print_error(cmd + " is not a valid command")
        else:
            # look up and print the manual
            print(user.io.OutputHandler.print_man(cmd))

    @staticmethod
    def print_error(error):
        """
        Alert the user to an error.
        """
        print("error: " + error)

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


class ImproperFormatException(Exception):
    """
    Custom exception thrown in the case of bad input.
    """

    def __init__(self, message):
        super().__init__(message)
