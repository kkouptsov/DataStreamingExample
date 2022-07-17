import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi

"""
Listens for connection from clients and saves
the data obtained from POST requests to a separate file
in TARGET_DIRECTORY.
"""

HOST = '127.0.0.1'
PORT = 8081
ROOT = os.path.dirname(os.path.realpath(__file__))
TARGET_DIRECTORY = 'out'

class PostHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_error(404)
        self.end_headers()

    def do_POST(self):
        """ Expect data in the form
            {'file' : data, 'file_name' : name, 'file_size' : size, 'counter' : num}
            where data is the raw contents of the file and the rest are metadata.
        """
        form = cgi.FieldStorage(
            fp = self.rfile, 
            headers = self.headers,
            environ = {
                'REQUEST_METHOD' : 'POST',
                'CONTENT_TYPE' : self.headers['Content-Type'],
            }
        )
        file_name = form['file_name'].value
        file_path = os.path.join(ROOT, TARGET_DIRECTORY, file_name)

        # TODO: use these e.g. to check the file and terminate the server
        file_size = form['file_size'].value
        counter = form['counter'].value 
 
        # TODO: use buffered read/write not to keep the whole file in memory
        data = form['file'].value
        with open(file_path, 'wb') as file:
            file.write(data)

        self.send_response(200, message = None)
        self.end_headers()

def main():
    server_address = (HOST, PORT)
    srv = HTTPServer(server_address, PostHandler)
    print('Starting the server... Use <Ctrl-C> or <Ctrl-Break> to terminate.')
    try:
        srv.serve_forever()
    except:
        pass
    print('Terminating the server.')
    srv.server_close()

if __name__ == "__main__":
    # TODO: handle argv, specify port, save directory etc.
    main()
