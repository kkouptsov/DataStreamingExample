import time, math, os
import numpy as np
from utils import randomFromRange, getArg

class FileGenerator:

    # Default parameters
    SOURCE_DIRECTORY = 'in'
    FILE_MIN_SIZE = 1024         # 1 KiB
    FILE_MAX_SIZE = 1024*1024    # 1 MiB

    # Some constants
    BUFFER_SIZE = 512
    DATA_TYPE = np.int16

    def __init__(self, **kwargs):
        self.source_dir = getArg(kwargs, 'target_dir', str, self.SOURCE_DIRECTORY)
        
    def makeFileSize(self):
        """ Calculate a random file size
        """
        return math.floor(randomFromRange(self.FILE_MIN_SIZE, self.FILE_MAX_SIZE))

    def makeFileName(self):
        """ Generate a random file name
        """
        return str(math.floor(1000 * time.time()))

    def createFile(self, file_name, file_size):
        """ Create a binary file and write 'filesize' random 'type' integers into it
        """
        file_path = os.path.join(self.source_dir, file_name)
        ii = np.iinfo(self.DATA_TYPE)
        max_chunk_size = self.BUFFER_SIZE
        with open(file_path, 'wb') as file:
            while file_size > 0:
                chunk_size = min(max_chunk_size, file_size)
                data = np.random.randint(ii.min, ii.max, size = chunk_size, dtype = self.DATA_TYPE)
                data_len = file.write(data)
                file_size = file_size - data_len

    def removeFile(self, file_name):
        file_path = os.path.join(self.source_dir, file_name)
        os.remove(file_path)
