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
        {"a": self.foo, "man": self.foo, "v": self.print_all, "x": self.stop}.get(args[0], self.__print_err)(args)

    def print_all(self, args=None):
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

    @staticmethod
    def __print_err(args):
        print("error: " + "".join(args) + " is not valid")

    def stop(self, args=None):
        self.__running = False

    def foo(self):
        pass
