import requests
import os

"""
Generates a file and once it is done sends the data over HTTP using POST
"""

ROOT = os.path.dirname(os.path.realpath(__file__))
SOURCE_DIRECTORY = 'in'

def main():
    try:
        infile = os.path.join(ROOT, SOURCE_DIRECTORY, 'aaa')
        files= {'file': ('aaa', open(infile, 'rb'), 'application/octet-stream')}
        response = requests.post('http://localhost:8081', files = files)
        print(response)
    except Exception as e:
        print("exception: ", e)

if __name__ == "__main__":
    main()
