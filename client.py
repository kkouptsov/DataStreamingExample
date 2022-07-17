import requests
import os

"""
Generates a file and once it is done sends the data over HTTP using POST
"""

HOST = '127.0.0.1'
PORT = 8081
ROOT = os.path.dirname(os.path.realpath(__file__))
SOURCE_DIRECTORY = 'in'

fg = FileGenerator(source_dir = os.path.join(ROOT, SOURCE_DIRECTORY))


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
    main()
