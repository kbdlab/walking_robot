# https://www.mixedcontentexamples.com
file = 'steveholt.jpg'
host = 'localhost:8000'

from http.client import HTTPConnection

with open(file, 'wb') as File:
    conn = HTTPConnection('www.mixedcontentexamples.com')
    conn.request("GET", "/Content/Test/steveholt.jpg")
    res = conn.getresponse()
    File.write(res.read())
    print('Downloaded to', file)

with open(file, 'rb') as File:
    conn = HTTPConnection(host)
    conn.request('POST', '/', body=File.read())
    res = conn.getresponse()
    print('Uploaded to', host, 'with status', res.status)