def _valid_name_(name):
    if not isinstance(name, str):
        raise TypeError("Table name must be a string")


def _valid_key_(key):
    if not isinstance(key, str):
        raise TypeError("Key name must be a string")