import json
from jdb.db import Database
from jdb.utils import _valid_key_


class KVStore(Database):

    def set(self, key, value):
        _valid_key_(key)
        self.db[key] = json.dumps(value.__dict__)

    def get(self, key):
        _valid_key_(key)
        return json.loads(self.db[key])

    def delete(self, key):
        _valid_key_(key)
        if key in self.db:
            del self.db[key]

    def exists(self, key):
        _valid_key_(key)
        return key in self.db

    def keys(self):
        return self.db.keys()

    def count(self):
        return len(self.db)
