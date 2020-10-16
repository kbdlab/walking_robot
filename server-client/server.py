PORT = 8000

from http.server import BaseHTTPRequestHandler
import socketserver
import json
from readchar import readchar


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        #self.send_header('Content-type','text/html')
        self.end_headers()
        print("write to stdin")
        while True:
            self.wfile.write(
                bytes(json.dumps({"action": readchar()}), encoding='utf8'))
            self.wfile.write(b'\n')


with socketserver.TCPServer(("localhost", PORT), Handler) as httpd:
    print("HTTPServer Serving at port", PORT)
    httpd.serve_forever()
