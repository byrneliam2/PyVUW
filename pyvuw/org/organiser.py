"""
Liam Byrne (byrneliam2)
PyVUW
"""


class Organiser:
    """
    The Organiser is the hub of the application. It provides a collection of courses
    and options to modify each course. The courses are referred to by name and their
    workloads are stored as lists within the dictionary that makes up the core of
    this class.
    """

    def __init__(self):
        self._courses = {}

    def __iter__(self):
        return iter(self._courses.items())

    def __len__(self):
        return len(self._courses)

    # ------------------------------------------------------------------------------

    def add_data(self, course, tasks):
        """
        Add a new course to the organiser. If tasks are present, those are immediately
        added into the newly built course. Note that the tasks argument is read into
        the organiser as the raw whitespace-separated list from the input.
        """
        if course not in self._courses.keys():
            self._courses[course] = tasks
        else:
            self._courses.get(course).extend(tasks)

    def del_data(self, course, tasks):
        """
        Remove either a course from the organiser, or if tasks are present,
        only the specified tasks. Note that the tasks argument is read into
        the organiser as the raw whitespace-separated list from the input.
        """
        if course not in self._courses.keys():
            return

        # no tasks? delete everything
        if len(tasks) == 0:
            del self._courses[course]
        else:
            deleted = 0
            for t in tasks:
                # check if the task is in index representation first
                if t.startswith("[") and t.endswith("]"):
                    # need to account for dynamic list length
                    # extra -1 for indexing from 1 for user ease
                    del self._courses.get(course)[int(t[1]) - deleted - 1]
                    deleted += 1
                if t not in self._courses.get(course):
                    continue
                else:
                    self._courses.get(course).remove(t)
                    deleted += 1

    def edit_data(self, course, old, new):
        """
        Edit an existing task within a course.
        """
        if course in self._courses.keys():
            tasks = self._courses.get(course)
            if old in tasks:
                tasks[tasks.index(old)] = new
        pass

    def do_by_index(self, tasks, func):
        for t in tasks:
            if t.startswith("[") and t.endswith("]"):
                func(t)

    def total_work(self):
        """
        Return the number of assignments, reports, etc. in total across all courses.
        """
        count = 0
        for work in self._courses.values():
            count += len(work)
        return count
