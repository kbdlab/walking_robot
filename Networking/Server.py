from http.server import BaseHTTPRequestHandler
import socketserver
import json
from readchar import readkey
from sys import argv
from os import environ

import numpy as np
import cv2

from utils import Time, PORT

DISPLAY = 'DISPLAY' in environ


class Handler(BaseHTTPRequestHandler):
    server = None

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        print("Write to stdin")
        while True:
            key = readkey()
            if key == '\x03':
                self.finish()
                self.server.shutdown()
                break

            data = {"action": key}
            print(Time(), 'Sending', data)
            self.wfile.write(bytes(json.dumps(data), encoding='utf8'))
            self.wfile.write(b'\n')

    def do_POST(self):
        print(self.headers['X-Client2Server'])

        self.send_response(200)
        self.send_header('X-Server2Client', '123')
        self.end_headers()

        data = self.rfile.read(int(self.headers['Content-Length']))
        img = np.asarray(bytearray(data), dtype="uint8")
        img = cv2.imdecode(img, cv2.IMREAD_ANYCOLOR)

        # Use img as an input of your autonomous driving code

        if DISPLAY:
            try:
                cv2.imshow('image', img)
                cv2.waitKey(1)
            except Exception as error:
                DISPLAY = False
                print(
                    'Following exception has been raised in imshow. Reverting to saving to a file'
                )
                print(error)

        else:
            with open('uploaded.jpg', 'wb') as File:
                File.write(data)
                print('Image has been written to file')

        self.wfile.write(bytes(json.dumps({"foo": "bar"}), encoding='utf8'))


if __name__ == '__main__':
    with socketserver.TCPServer(("0.0.0.0", PORT),
                                Handler,
                                bind_and_activate=False) as httpd:
        httpd.server = httpd
        httpd.allow_reuse_address = True
        httpd.server_bind()
        httpd.server_activate()
        print("HTTPServer Serving at port", PORT)
        httpd.serve_forever()
