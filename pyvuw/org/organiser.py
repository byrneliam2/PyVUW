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

    def add_course(self, name, work):
        """
        Add a new course to the organiser.
        :param name: course name
        :param work: list of work associated with course
        """
        #work.append(Assignment(name, "never"))
        self.__courses[name] = work

    def del_course(self, name):
        """
        Remove a course from the organiser.
        :param name: name of the course
        """
        if name in self.__courses.keys():
            del self.__courses[name]

    def total_work(self):
        """
        Return the number of assignments, reports, etc. in total across all courses.
        :return: number of tasks
        """
        count = 0
        for list in self.__courses.values():
            count += len(list)
        return count
