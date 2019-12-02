import cv2
import numpy as np
import time
import math
import glob
import os
import image_process as img
import decision

if __name__ == "__main__":
    start_time=time.time()
    path = './image_set/*.png'
    file_list = glob.glob(path)
    cnt = 0
    for i in file_list:        
        image = cv2.imread(i)
        name, extension = os.path.splitext(os.path.basename(i))
        masked_image=img.region_of_interest(decision.select_white(image,160))
        result=decision.set_path3(masked_image, 0.25)
        
        if result[0][0] in name[-3:]:
            answer = '○'
            cnt += 1
        else:
            answer = '×'
        
        print(name, answer, result) 
        
        # draw line, set_path_3
        
        y1, x1 = masked_image.shape
        x1 = int(x1/2)
        x2 = int(-result[2] * result[1] + x1)
        y2 = y1-result[2]
        cv2.line(image,(x1,y1),(x2,y2),(0,0,255),2)  
        cv2.line(masked_image,(x1,y1),(x2,y2),(100),2)    
        
        cv2.imshow('image', image)
        cv2.imshow('white', masked_image)
        key = cv2.waitKey(0)

        if key == ord('q'):
            break
        
             
        
    cv2.destroyAllWindows()
    print('\nTotal:', str(len(file_list)))
    print('Acurracy:', str(round(100*cnt/len(file_list), 2))+" %")