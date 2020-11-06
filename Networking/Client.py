PORT = 8000

from http.client import HTTPConnection
import json
from time import sleep

from Time import Time
from sys import argv

print(argv)

def main():
    while True:
        conn = HTTPConnection(f"{argv[1] if len(argv) > 1 else  'localhost'}:{PORT}")

        try:
            conn.request("GET", "/")
        except ConnectionRefusedError as error:
            print(error)
            sleep(1)
            continue

        print('Connected')
        res = conn.getresponse()
        while True:
            chunk = res.readline()
            if (chunk == b'\n'): continue
            if (not chunk): break

            chunk = chunk[:-1].decode()
            print(Time(), json.loads(chunk))


main()
