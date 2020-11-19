# https://www.mixedcontentexamples.com
file = 'steveholt.jpg'
host = 'localhost:8000'

from http.client import HTTPConnection
import numpy as np
import cv2


def Upload(body):
    conn = HTTPConnection(host)
    conn.request('POST', '/', body=body)
    res = conn.getresponse()
    print('Uploaded to', host, 'with status', res.status)

def DownloadAndUpload():
    with open(file, 'wb') as File:
        conn = HTTPConnection('www.mixedcontentexamples.com')
        conn.request("GET", "/Content/Test/steveholt.jpg")
        res = conn.getresponse()
        File.write(res.read())
        print('Downloaded to', file)

    with open(file, 'rb') as File:
        Upload(File.read())

def UploadNumpy():
    img = np.random.random((100, 100,3))
    print('shape', img.shape)
    result, img = cv2.imencode('.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
    if not result:
        raise Exception('Image encode error')
    Upload(img.tobytes())

if __name__ == '__main__':
    #DownloadAndUpload()
    UploadNumpy()
