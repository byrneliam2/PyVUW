"""
Liam Byrne (byrneliam2)
PyVUW
"""

import user.io


class UI:

    # Printing constants
    NUM_TNAME = 10

    # Execution
    running = True

    def __init__(self, org):
        self._org = org
        self.print_all()

    def do_next(self):
        """
        Take a user input and perform the operation it translates to, if it is correct.
        """

        # get the input and split into a list of arguments
        args = input("> ").split()

        # no input, no response
        if len(args) == 0:
            return

        # commands with arguments
        if args[0] == "a":
            self._org.add_data(args[1], args[2:])
        elif args[0] == "del":
            self._org.del_data(args[1], args[2:])

        # no argument commands
        elif args[0] == "man":
            self.print_man()
        elif args[0] == "s":
            user.io.OutputHandler.write_out(self._org)
        elif args[0] == "v":
            self.print_all()
        elif args[0] == "x":
            self.running = False

        else:
            # it must be an invalid command
            print("error: command " + args[0] + " is not valid")

    @staticmethod
    def print_man():
        """
        Print the manual from the predefined file.
        """
        with open("store/man.txt", 'r') as man:
            print(man.read())

    def print_all(self):
        """
        Reprint the entire organiser.
        """

        print("=" * self.NUM_TNAME + " PyVUW Organiser " + "=" * self.NUM_TNAME)
        print()
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
