import cv2

import numpy as np

import sys



# You should replace these 3 lines with the output in calibration step

DIM=(320, 240)

K=np.array([[93.16858864610276, 0.0, 150.8535602775792], [0.0, 91.92373264897513, 146.22342371914382], [0.0, 0.0, 1.0]])

D=np.array([[0.14136243954038377], [0.29925561973923737], [-0.321789761587799], [0.11936916962615352]])

def undistort(img_path):

    img = cv2.imread(img_path)

    h,w = img.shape[:2]

    map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)

    undistorted_img = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)

    cv2.imshow("undistorted", undistorted_img)

    cv2.waitKey(0)

    cv2.destroyAllWindows()

    

    np.save('map1.npy',map1)

    np.save('map2.npy',map2)

    

    

if __name__ == '__main__':   

    undistort('./calibrate/img_1.jpg')