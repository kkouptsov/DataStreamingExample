import time, math, os
def time2ms(time):
    """ Helper function to convert time.time() to milliseconds
    """
    return math.floor(1000 * time)

def getArg(kw, name, cast, default):
    """ Get the value of the corresponding key making sure it
    has a correct type. Treat incorrect type as a missing value
    and return the default.
    """
    res = kw.get(name, default)
    if isinstance(res, cast):
        return res
    return default


class FileGenerator:

    # Default parameters
    TARGET_DIRECTORY = 'in'
    FILE_COUNT = 100
    FILE_MIN_SIZE = 1024         # 1 KiB
    FILE_MAX_SIZE = 1024*1024    # 1 MiB
    TIME_DURATION = 600*10**3    # 10 min
    TIME_MIN = 1                 # 1 ms
    TIME_MAX = 10**3             # 1 s

    def __init__(self, **kw):
        self.start_time = time2ms(time.time())
        self.end_time = self.start_time + getArg(kw, 'duration', int, self.TIME_DURATION)
        self.next_time = self.start_time
        self.count = self.FILE_COUNT
        self.outdir = os.path.abspath(getArg(kw, 'input_dir', str, self.TARGET_DIRECTORY))

