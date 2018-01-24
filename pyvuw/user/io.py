"""
Liam Byrne (byrneliam2)
PyVUW
"""

import json
from org.organiser import Organiser

JSON_NAME = "store/org.json"


class PyVUWInputStream:

    @staticmethod
    def read_in():
        org = Organiser()
        with open(JSON_NAME, 'r') as js:
            js_dict = json.load(js)
        if len(js_dict) == 0:
            return org
        org_dict = js_dict["_courses"]
        for course, work in org_dict.items():
            org.add_data(course, work)
        return org


class PyVUWOutputStream:

    @staticmethod
    def write_out(org):
        with open(JSON_NAME, 'w') as out:
            json.dump(org.__dict__, out, default=lambda obj: obj.__dict__, indent=1)
