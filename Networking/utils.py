from sys import argv
import datetime

print(argv)

PORT = 8000
SERVER = f"{argv[1] if len(argv) > 1 else  'localhost'}:{PORT}"
Time = lambda: datetime.datetime.now().time()

print('Server address', SERVER)
