"""
Liam Byrne (byrneliam2)
PyVUW
"""

import json
from pyvuw.org.organiser import Organiser

JSON_NAME = "store.json"


class PyVUWInputStream:

    @staticmethod
    def read_in():
        org = Organiser()
        with open(JSON_NAME, 'r') as js:
            js_dc = json.load(js)
        org_dc = js_dc["_Organiser__courses"]
        for c, w in org_dc.items():
            org.add_course(c, w)
        return org


class PyVUWOutputStream:

    @staticmethod
    def send_out(org):
        with open(JSON_NAME, 'w') as out:
            json.dump(org.__dict__, out, default=lambda x: x.__dict__, indent=1)
