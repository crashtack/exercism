#
# Skeleton file for the Python "Hello World" exercise.
#


def hello(name=None):
    """ Prints Hello, World!, or a costom greating if a name
        is passed in."""
    if name == '' or name is None:
        return 'Hello, World!'
    else:
        return 'Hello, {}!'.format(name)
