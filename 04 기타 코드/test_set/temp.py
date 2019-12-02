import cv2
import numpy as np

image_name = 'img_2c.jpg'
image = cv2.imread(image_name,0)
edges = cv2.Canny(image,100,200)

out = np.hstack((image, edges))
try:
    cv2.imshow('Image', out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except Exception as e:
    print(e)
