import requests
import os, time, math
import asyncio
from filegenerator import FileGenerator
from utils import randomFromRange

#
# Generates a file and then sends the data over HTTP using POST
#

HOST = '127.0.0.1'
PORT = 8081
ROOT = os.path.dirname(os.path.realpath(__file__))
SOURCE_DIRECTORY = 'in'

fg = FileGenerator(target_dir = os.path.join(ROOT, SOURCE_DIRECTORY))

FILE_COUNT = 100
TIME_DURATION = 600          # 10 min
TIME_MIN = 10**-3            # 1 ms
TIME_MAX = 1                 # 1 s

start_time = time.time()
end_time = start_time + TIME_DURATION
next_time = start_time

def getNextTime():
    """ Calculate a random time interval between successive file creation.
    Given that min and max times differ by a few orders of magnitude, it makes
    sense to generate time intervals using a non-uniform distribution
    """
    global next_time
    now = time.time()
    if now <= next_time:
        return now
    next_time = randomFromRange(TIME_MIN, min(TIME_MAX, end_time - now))
    return next_time

async def sendFile(file_name):
    file_path = os.path.join(ROOT, SOURCE_DIRECTORY, file_name)
    file_size = os.path.getsize(file_path)
    files = {'file': open(file_path, 'rb')}
    data = {'file_name' : file_name, 'file_size': file_size , 'counter' : 1}
    response = requests.post('http://' + HOST + ':' + str(PORT), files = files, data = data)
    return response.ok

async def createFile():
    timeout = getNextTime()
    print('timeout: ', timeout)
    await asyncio.sleep(timeout)
    file_name = fg.makeFileName()
    file_size = fg.makeFileSize()
    fg.createFile(file_name, file_size)
    return file_name

async def main():
    count = FILE_COUNT
    while count > 0:
        file_name = await createFile()
        await sendFile(file_name)
        count = count - 1

if __name__ == "__main__":
    # TODO: use argv to specify directory for files, parameters for file generation etc.
    asyncio.run(main())
