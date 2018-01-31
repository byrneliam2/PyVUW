"""
Liam Byrne (byrneliam2)
PyVUW
"""

from user.io import OutputHandler


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

        # determine action from input
        # commands with arguments
        if args[0] == "a":
            self._org.add_data(args[1], args[2:])
        elif args[0] == "del":
            # special case: either we can delete by specifying the exact string to delete
            # or the index of the item to delete
            if args[1].startswith("["):
                pass
            self._org.del_data(args[1], args[2:])
        # no argument commands
        elif args[0] == "man":
            self.print_man()
        elif args[0] == "s":
            OutputHandler.write_out(self._org)
        elif args[0] == "v":
            self.print_all()
        elif args[0] == "x":
            self.running = False
        else:
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

        def print_lines(n_name, n_work):
            print("-" * n_name, end='')
            print("-" * n_work * len(work))

        print("=" * self.NUM_TNAME + " PyVUW Organiser " + "=" * self.NUM_TNAME)
        print()
        print("(" + str(len(self._org)) + " courses, " + str(self._org.total_work()) + " tasks)")
        for name, work in self._org:
            print_lines(10, 4)
            print(name + ": ", end='')
            for w in work:
                print(w + " ", end='')
            print()
            print_lines(10, 4)
