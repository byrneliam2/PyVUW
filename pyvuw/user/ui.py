"""
Liam Byrne (byrneliam2)
PyVUW
"""


class UI:

    NUM_TNAME = 10
    NUM_CNAME = 10
    NUM_CWORK = 4

    __running = True

    def __init__(self, org):
        self.__org = org

        self.print_all()

    def is_running(self):
        return self.__running

    def do_next(self):
        """
        Take a user input and perform the operation it translates to, if it is correct.
        """
        # TODO add command line argument support as commands
        args = input("> ").split()
        if args[0] == "a":
            self.__org.add_data(args[1:])
        elif args[0] == "del":
            self.__org.del_data(args[1:])
        elif args[0] == "man":
            self.print_man()
        elif args[0] == "v":
            self.print_all()
        elif args[0] == "x":
            self.stop()
        else:
            self.__print_err(args)

    @staticmethod
    def print_man():
        with open("man.txt", 'r') as man:
            print(man.read())

    def print_all(self):
        """
        Reprint the entire organiser.
        """
        print("=" * self.NUM_TNAME + " PyVUW Organiser " + "=" * self.NUM_TNAME)
        print()
        print("(" + str(len(self.__org)) + " courses, " + str(self.__org.total_work()) + " tasks)")
        for name, work in self.__org:
            print("-" * self.NUM_CNAME, end='')
            print("-" * len(work))
            print(name)
            print("-" * self.NUM_CNAME, end='')
            print("-" * len(work))

    def stop(self):
        self.__running = False

    @staticmethod
    def __print_err(args):
        print("error: " + "".join(args) + " is not valid")
