import json
from jdb.db import Database
from jdb.utils import _valid_name_, _valid_key_


class DBTable(Database):

    def __init__(self, table_name, location=None):
        super().__init__(location)
        self._create_(table_name)

    def _create_(self, name):
        _valid_name_(name)
        self.db[name] = {}
        self.table_name = name

    def insert(self, key, value):
        _valid_key_(key)
        self.db[self.table_name][key] = json.dumps(value.__dict__)

    def select(self, key):
        _valid_key_(key)
        return self.db[self.table_name][key]

    def delete(self, key):
        _valid_key_(key)
        del self.db[self.table_name][key]

    def exists(self, key):
        _valid_key_(key)
        return key in self.db[self.table_name]

    def count(self):
        return len(self.db[self.table_name])

    def select_all(self):
        return self.db[self.table_name]
