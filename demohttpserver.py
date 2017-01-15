#!/usr/bin/env python

import sys
import os
if sys.version_info >= (3, 0):
    from http.server import BaseHTTPRequestHandler, HTTPServer
else:
    from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def set_headers(self, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

    def do_GET(self):
        if self.path == '/ping':
            self.set_headers()
            self.wfile.write(b'pong')
        elif self.path == '/kill':
            self.set_headers(status=500)
            self.wfile.write(b'killed')
            os._exit(1)
        else:
            self.set_headers(status=404)
            self.wfile.write(b'404 Not Found')

def run(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, MyHandler)
    print('Starting HTTP server on port {}...'.format(port))
    httpd.serve_forever()

if __name__ == "__main__":
    if len(sys.argv) == 2:
        run(port=int(sys.argv[1]))
    else:
        run()

