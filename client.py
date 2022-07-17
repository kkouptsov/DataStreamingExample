import requests
from utils import randomFromRange

#
# Generates a file and then sends the data over HTTP using POST
#

HOST = '127.0.0.1'
PORT = 8081
ROOT = os.path.dirname(os.path.realpath(__file__))
SOURCE_DIRECTORY = 'in'

fg = FileGenerator(target_dir = os.path.join(ROOT, SOURCE_DIRECTORY))


TIME_DURATION = 600*10**3    # 10 min
TIME_MIN = 1                 # 1 ms
TIME_MAX = 10**3             # 1 s

start_time = time2ms(time.time())
end_time = start_time + TIME_DURATION
next_time = start_time

def getNextTime(self):
    """ Calculate a random time interval between successive file creation.
    Given that min and max times differ by a few orders of magnitude, it makes
    sense to generate time intervals using a non-uniform distribution
    """
    now = time2ms(time.time())
    if now > self.next_time:
        return randomFromRange(self.TIME_MIN, math.min(self.TIME_MAX, self.end_time - now))

def sendFile(file_name):
    file_path = os.path.join(ROOT, SOURCE_DIRECTORY, file_name)
    file_size = os.path.getsize(file_path)
    files = {'file': open(file_path, 'rb')}
    data = {'file_name' : file_name, 'file_size': file_size , 'counter' : 1}
    response = requests.post('http://' + HOST + ':' + str(PORT), files = files, data = data)
    return response.ok

def createFile():
    file_name = fg.makeFileName()
    file_size = fg.makeFileSize()
    fg.createFile(file_name, file_size)
    return file_name

def main():
    try:
        file_name = createFile()
        sendFile(file_name)

    except Exception as e:
        print("exception: ", e)

if __name__ == "__main__":
    # TODO: use argv to specify directory for files, parameters for file generation etc.
    main()
