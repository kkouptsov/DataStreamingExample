import time, math, os
import numpy as np

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

def randomFromRange(min, max):
    """ Get a random point from the interval with descreasing probability.
    Using a suitable but arbitrary chosen distribution. This could be improved. 
    """
    res = min + np.random.exponential((max - min)/5)
    while res > max:
        res = min + np.random.exponential((max - min)/5)
    return res


class FileGenerator:

    # Default parameters
    SOURCE_DIRECTORY = 'in'
    FILE_COUNT = 100
    FILE_MIN_SIZE = 1024         # 1 KiB
    FILE_MAX_SIZE = 1024*1024    # 1 MiB
    TIME_DURATION = 600*10**3    # 10 min
    TIME_MIN = 1                 # 1 ms
    TIME_MAX = 10**3             # 1 s

    # Some constants
    BUFFER_SIZE = 512
    DATA_TYPE = np.int16

    def __init__(self, **kw):
        self.start_time = time2ms(time.time())
        self.end_time = self.start_time + getArg(kw, 'duration', int, self.TIME_DURATION)
        self.next_time = self.start_time
        self.count = self.FILE_COUNT
        self.indir = os.path.abspath(getArg(kw, 'input_dir', str, self.SOURCE_DIRECTORY))

    def getNextTime(self):
        """ Calculate a random time interval between successive file creation.
        Given that min and max times differ by a few orders of magnitude, it makes
        sense to generate time intervals using a non-uniform distribution
        """
        now = time2ms(time.time())
        if now > self.next_time:
            return randomFromRange(self.TIME_MIN, math.min(self.TIME_MAX, self.end_time - now))
        
    def makeFileSize(self):
        """ Calculate a random file size
        """
        return math.floor(randomFromRange(self.FILE_MIN_SIZE, self.FILE_MAX_SIZE))

    def makeFileName(self):
        """ Generate a random file name
        """
        return os.path.join(self.indir, str(time2ms(time.time())))

    def createFile(self, filepath, filesize):
        """ Create a binary file and write 'filesize' random 'type' integers into it
        """
        ii = np.iinfo(self.DATA_TYPE)
        max_chunk_size = self.BUFFER_SIZE
        with open(filepath, 'wb') as file:
            while filesize > 0:
                chunk_size = min(max_chunk_size, filesize)
                data = np.random.randint(ii.min, ii.max, size = chunk_size, dtype = self.DATA_TYPE)
                data_len = file.write(data)
                filesize = filesize - data_len

    def removeFile(self, filepath):
        # TODO: make safe, delete only from 'indir'
        os.remove(filepath)
