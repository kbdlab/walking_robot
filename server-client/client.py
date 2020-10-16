from http.client import HTTPConnection
import json
from time import sleep


def main():
    while True:
        conn = HTTPConnection('localhost:8000')

        try:
            conn.request("GET", "/")
        except ConnectionRefusedError as error:
            print(error)
            sleep(1)
            continue

        print('Connected')
        r1 = conn.getresponse()
        while True:
            chunk = r1.readline()
            if (chunk == b'\n'): continue
            if (not chunk): break

            chunk = chunk[:-1].decode()
            print(json.loads(chunk))


main()
