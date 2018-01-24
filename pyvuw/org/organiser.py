"""
Liam Byrne (byrneliam2)
PyVUW
"""


class Organiser:
    """
    The Organiser is the hub of the application. It provides a collection of courses
    and options to modify each course. The courses are referred to by name and their
    workloads are stored as variations of the Coursework class.
    """

    def __init__(self):
        self._courses = {}

    def __iter__(self):
        return iter(self._courses.items())

    def __len__(self):
        return len(self._courses)

    # ------------------------------------------------------------------------------

    def add_data(self, course, work):
        """
        Add a new course to the organiser. Note that the work argument is read into
        the organiser as a whitespace-separated list from the given arguments.
        """
        if course not in self._courses.keys():
            self._courses[course] = work
        else:
            self._courses.get(course).extend(work)

    def del_data(self, course, work):
        """
        Remove a course from the organiser. Note that the work argument is read into
        the organiser as a whitespace-separated list from the given arguments.
        """
        if course in self._courses.keys():
            if len(work) == 0:
                del self._courses[course]
            else:
                for d in work:
                    self._courses.get(course).remove(d)

    def total_work(self):
        """
        Return the number of assignments, reports, etc. in total across all courses.
        :return: number of tasks
        """
        count = 0
        for work in self._courses.values():
            count += len(work)
        return count
