"""
Liam Byrne (byrneliam2)
PyVUW
"""

import user.io

from user.ui import UI


class Main:
    """
    Main runner class for the PyVUW application. Loops the execution of the
    user input control until a terminate command is sent.
    """

    def __init__(self):
        self.org = user.io.InputHandler.read_in()
        self.ui = UI(self.org)
        while self.ui.running:
            self.ui.do_next()
        user.io.OutputHandler.write_out(self.org)


# start
if __name__ == "__main__":
    Main()
