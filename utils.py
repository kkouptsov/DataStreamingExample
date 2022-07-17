import numpy as np

def randomFromRange(min, max):
    """ Get a random point from the interval with descreasing probability.
    Using a suitable but arbitrary chosen distribution. This could be improved.

    TODO: should be in a separate file, utils.py
    """
    res = min + np.random.exponential((max - min)/5)
    while res > max:
        res = min + np.random.exponential((max - min)/5)
    return res

def getArg(kw, name, cast, default):
    """ Get the value of the corresponding key making sure it
    has a correct type. Treat incorrect type as a missing value
    and return the default.

    TODO: elminate it
    """
    res = kw.get(name, default)
    if isinstance(res, cast):
        return res
    return default
