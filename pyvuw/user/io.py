"""
Liam Byrne (byrneliam2)
PyVUW
"""

import json
import os

from org.organiser import Organiser

JSON_NAME = "org.json"
MAN_NAME = "man.txt"
STORE = os.path.dirname(__file__) + "/../store/"


class InputHandler:

    @staticmethod
    def eval_input(args):
        pass

    @staticmethod
    def read_in():
        org = Organiser()
        with open(os.path.join(STORE, JSON_NAME), 'r') as js:
            js_dict = json.load(js)
        if len(js_dict) == 0:
            return org
        org_dict = js_dict["_courses"]
        for course, tasks in org_dict.items():
            org.add_data(course, tasks)
        return org


class OutputHandler:

    @staticmethod
    def write_out(org):
        with open(os.path.join(STORE, JSON_NAME), 'w') as out:
            json.dump(org.__dict__, out, default=lambda obj: obj.__dict__, indent=1)

    @staticmethod
    def write_man():
        with open(os.path.join(STORE, MAN_NAME), 'r') as man:
            return man.read()
