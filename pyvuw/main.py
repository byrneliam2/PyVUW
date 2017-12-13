"""
Liam Byrne (byrneliam2)
PyVUW
"""

from pyvuw.ui.ui import UI
from pyvuw.ui.io import *


class Main:
    """
    Main runner class for the PyVUW application.
    """

    def __init__(self):
        self.org = PyVUWInputStream.read_in()
        self.ui = UI(self.org)
        while self.ui.is_running():
            self.ui.do_next()
        PyVUWOutputStream.send_out(self.org)


# start
if __name__ == "__main__":
    Main()
