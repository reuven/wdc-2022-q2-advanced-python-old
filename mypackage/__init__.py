# this file, __init__.py, will be run automatically when someone
# imports mypackage

from . import a
from . import b

print('Hello from mypackage!')

print(a.hello('world'))
