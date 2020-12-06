# https://www.mixedcontentexamples.com
file = 'steveholt.jpg'

from http.client import HTTPConnection
import numpy as np
import cv2

from utils import SERVER, Time


def Upload(body, headers={}):
    conn = HTTPConnection(SERVER)
    conn.request('POST', '/', body=body, headers=headers)
    res = conn.getresponse()
    print(res.getheaders())
    print(res.getheader('X-Server2Client', 'Fallback'))
    print(res.read())
    print('Uploaded to', SERVER, 'with status', res.status)


def Download():
    with open(file, 'wb') as File:
        conn = HTTPConnection('www.mixedcontentexamples.com')
        conn.request("GET", "/Content/Test/steveholt.jpg")
        res = conn.getresponse()
        File.write(res.read())
        print('Downloaded to', file)


def DownloadAndUpload():
    Download()
    with open(file, 'rb') as File:
        Upload(File.read())


def UploadNumpy(ndarray):
    print('shape', ndarray.shape)
    result, img = cv2.imencode('.jpg', img,
                               [int(cv2.IMWRITE_JPEG_QUALITY), 90])
    if not result:
        raise Exception('Image encode error')

    Upload(img.tobytes(), {"X-Client2Server": "123"})


if __name__ == '__main__':
    #Download()
    #DownloadAndUpload()
    UploadNumpy(255 * np.random.random((100, 100, 3)))
