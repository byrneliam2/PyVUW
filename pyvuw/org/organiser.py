"""
Liam Byrne (byrneliam2)
PyVUW
"""


class Organiser:
    """
    The Organiser is the hub of the application. It provides a collection of courses
    and options to modify each course. The courses are referred to by name and their
    workloads are stored a variation of the Coursework class.
    """

    def __init__(self):
        self.__courses = {}

    def __iter__(self):
        return iter(self.__courses.items())

    def __len__(self):
        return len(self.__courses)

    def add_data(self, args):
        """
        Add a new course to the organiser.
        """
        if len(args) == 1:
            self.__courses[args[0]] = []
        elif len(args) == 2:
            if args[0] not in self.__courses.keys():
                self.__courses[args[0]] = [args[1]]
            else:
                self.__courses.get(args[0]).append(args[1])

    def del_data(self, args):
        """
        Remove a course from the organiser.
        """
        if args[0] in self.__courses.keys():
            if len(args) == 1:
                del self.__courses[args[0]]
            elif len(args) == 2:
                self.__courses[args[0]].remove(args[1])

    def total_work(self):
        """
        Return the number of assignments, reports, etc. in total across all courses.
        :return: number of tasks
        """
        count = 0
        for list in self.__courses.values():
            count += len(list)
        return count
