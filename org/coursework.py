"""
Liam Byrne (byrneliam2)
PyVUW
"""


class Coursework:
    """
    The Coursework class is the root of the Coursework hierarchy. There are many types
    of Coursework that the user can assign to Courses.
    """

    def __init__(self, course, due):
        self.course = course
        self.due = due


class Assignment(Coursework):
    """
    Represents an Assignment.
    """

    def __init__(self, course, due):
        super().__init__(course, due)


class Report(Coursework):
    """
    Represents a Report.
    """

    def __init__(self, course, due):
        super().__init__(course, due)
