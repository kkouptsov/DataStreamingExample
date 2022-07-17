import requests
import os

"""
Generates a file and once it is done sends the data over HTTP using POST
"""

ROOT = os.path.dirname(os.path.realpath(__file__))
SOURCE_DIRECTORY = 'in'

def main():
    try:
        file_path = os.path.join(ROOT, SOURCE_DIRECTORY, 'aaa')
        file_size = os.path.getsize(file_path)
        files = {'file': open(file_path, 'rb')}
        data = {'file_name' : 'aaa', 'file_size': file_size , 'counter' : 1}
        response = requests.post('http://localhost:8081', files = files, data = data)
        print(response)

    except Exception as e:
        print("exception: ", e)

if __name__ == "__main__":
    main()
