"""
Liam Byrne (byrneliam2)
PyVUW
"""

from user.io import PyVUWOutputStream


class UI:

    # Printing constants
    NUM_TNAME = 10
    NUM_CNAME = 10
    NUM_CWORK = 4

    # Execution
    running = True

    def __init__(self, org):
        self._org = org
        self.print_all()

    def do_next(self):
        """
        Take a user input and perform the operation it translates to, if it is correct.
        TODO split this out to a controller?
        """
        args = input("> ").split()
        if args[0] == "a":
            self._org.add_data(args[1], args[2:])
        elif args[0] == "del":
            self._org.del_data(args[1], args[2:])
        elif args[0] == "man":
            self.print_man()
        elif args[0] == "s":
            PyVUWOutputStream.write_out(self._org)
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
        print("=" * self.NUM_TNAME + " PyVUW Organiser " + "=" * self.NUM_TNAME)
        print()
        print("(" + str(len(self._org)) + " courses, " + str(self._org.total_work()) + " tasks)")
        for name, work in self._org:
            print("-" * self.NUM_CNAME, end='')
            print("-" * self.NUM_CWORK * len(work))
            print(name + ": ", end='')
            for w in work:
                print(w + " ", end='')
            print()
            print("-" * self.NUM_CNAME, end='')
            print("-" * self.NUM_CWORK * len(work))
