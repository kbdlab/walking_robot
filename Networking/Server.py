PORT = 8000

from http.server import BaseHTTPRequestHandler
import socketserver
import json
from readchar import readkey
from sys import argv
from os import environ

import numpy as np
import cv2

from Time import Time

httpd = None
DISPLAY = 'DISPLAY' in environ

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()

        print("Write to stdin")
        while True:
            key = readkey()
            if key == '\x03':
                break

            data = {"action": key}
            print(Time(), 'Sending', data)
            self.wfile.write(
                bytes(json.dumps(data), encoding='utf8'))
            self.wfile.write(b'\n')

        self.finish()
        httpd.shutdown()


    def do_POST(self):
        print(self.headers['X-Client2Server'])

        self.send_response(200)
        self.send_header('X-Server2Client', '123')
        self.end_headers()

        data = self.rfile.read(int(self.headers['Content-Length']))
        if DISPLAY:
            data = np.asarray(bytearray(data), dtype="uint8")
            img = cv2.imdecode(data, cv2.IMREAD_ANYCOLOR)
            #Marker
            cv2.imshow('image', img)
            cv2.waitKey(1)

        else:
            with open('uploaded.jpg', 'wb') as File:
                File.write(data)
                print('Written to file')

        self.wfile.write(
                bytes(json.dumps({"foo": "bar"}), encoding='utf8'))



with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as _httpd:
    httpd = _httpd
    print("HTTPServer Serving at port", PORT)
    httpd.serve_forever()
