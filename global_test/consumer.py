import service
global _properties
_properties = 'qrt'

try:
    _properties
except Exception as ex:
    print("exception")
print('_properties' in globals())
