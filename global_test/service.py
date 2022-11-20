try:
    _properties
except NameError as ex:
    _properties = None
    print(ex)

def properties():
    global _properties
    if not _properties:
        _properties = 'abc'
    return _properties