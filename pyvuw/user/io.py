"""
Liam Byrne (byrneliam2)
PyVUW
"""

import json
import os

from org.organiser import Organiser

STORE_NAME = os.path.dirname(__file__) + "/../store/"
JSON_NAME = "org.json"
MANS_NAME = "mans/"


class InputHandler:

    @staticmethod
    def eval_input(args):
        pass

    @staticmethod
    def read_in():
        org = Organiser()
        with open(os.path.join(STORE_NAME, JSON_NAME), 'r') as js:
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
        with open(os.path.join(STORE_NAME, JSON_NAME), 'w') as out:
            json.dump(org.__dict__, out, default=lambda obj: obj.__dict__, indent=1)

    @staticmethod
    def list_mans():
        mans = []
        for file in os.listdir(os.path.join(STORE_NAME, MANS_NAME)):
            if file.endswith(".txt"):
                name = file.replace(".txt", "")
                mans.append(name)
        return mans

    @staticmethod
    def print_man(man_name):
        with open(os.path.join(STORE_NAME, MANS_NAME + man_name + ".txt"), 'r') as man:
            return man.read()
