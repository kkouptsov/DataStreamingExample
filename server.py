import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi

"""
Listens for connection from clients and saves
the data obtained from GET requests to a separate file
in TARGET_DIRECTORY.
"""

HOST = '127.0.0.1'
PORT = 8081
ROOT = os.path.dirname(os.path.realpath(__file__))
TARGET_DIRECTORY = 'out'

class PostHandler(BaseHTTPRequestHandler):
    def __init__(self, *args):
        self.outdir = os.path.join(ROOT, TARGET_DIRECTORY)
        super(PostHandler, self).__init__(*args)

    def do_GET(self):
        self.send_error(404)
        self.end_headers()

    def do_POST(self):
        # TODO: process form fields  XXXXX
        filename = os.path.join(self.outdir, 'aaa')
        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length)
        print("content_length: ", content_length)
        with open(os.path.join(self.outdir, filename), 'wb') as file:
            file.write(data)
        self.send_response(200, message = None)
        self.end_headers()

def main():
    server_address = (HOST, PORT)
    srv = HTTPServer(server_address, PostHandler)
    print('Starting the server, use <Ctrl-C> or <Ctrl-Break> to terminate...')
    try:
        srv.serve_forever()
    except:
        pass
    print('Terminating the server.')
    srv.server_close()

if __name__ == "__main__":
    # TODO: handle argv, specify port, save directory etc.
    main()
