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
    def read_in():
        """
        Read the org.json file to generate an organiser object.
        :return: new organiser if JSON file has no courses recorded, or one with the date from the file
        recorded in otherwise
        """
        org = Organiser()
        with open(os.path.join(STORE_NAME, JSON_NAME), 'r') as js:
            js_dict = json.load(js)
        if len(js_dict) == 0:
            # no data, return new organiser as is
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
        """
        Generate and return a list of all current manual files in the store/mans directory.
        :return: list of manual file names
        """
        mans = []
        for file in os.listdir(os.path.join(STORE_NAME, MANS_NAME)):
            if file.endswith(".txt"):
                mans.append(file.split(".")[0])
        return mans

    @staticmethod
    def print_man(cmd):
        with open(os.path.join(STORE_NAME, MANS_NAME + cmd + ".txt"), 'r') as man:
            return man.read()
