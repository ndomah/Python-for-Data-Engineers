import os
import json


class Database(object):
    def __init__(self, location=None):
        if location:
            self.db_location = location
            self._load_()
        else:
            self.db = {}

    def _load_(self):
        if os.path.exists(self.db_location):
            db_file = open(self.db_location, "r")
            self.db = json.load(db_file)
        else:
            self.db = {}

    def save(self, location=None):
        if location:
            db_file = open(location, "w")
        elif self.db_location:
            db_file = open(self.db_location, "w")
        else:
            raise ValueError("DB location is null")

        json.dump(self.db, db_file)
        db_file.close()
