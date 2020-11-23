from sys import argv
import numpy as np
from timeit import timeit
from time import sleep, time
from cv2 import imwrite

def Fractal(size):
    # Remove this function body and write yours here
    img = 255 * np.random.random((size, size, 3))
    sleep(1)
    return img

def main(size):
    t = time()
    img = Fractal(size)
    t = time() - t
    imwrite(str(size) + '.jpg', img)
    return t

if __name__ == '__main__':
    a = main(100)
    b = main(1000)
    print(b/a, a, b)