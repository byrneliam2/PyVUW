"""
Liam Byrne (byrneliam2)
PyVUW
"""

import json
from org.organiser import Organiser

JSON_NAME = "store.json"


class PyVUWInputStream:

    @staticmethod
    def read_in():
        org = Organiser()
        with open(JSON_NAME, 'r') as js:
            js_dict = json.load(js)
        org_dict = js_dict["_Organiser__courses"]
        for course, work in org_dict.items():
            org.add_course(course, work)
        return org


class PyVUWOutputStream:

    @staticmethod
    def send_out(org):
        with open(JSON_NAME, 'w') as out:
            json.dump(org.__dict__, out, default=lambda x: x.__dict__, indent=1)
