import cv2
import time
import glob
import os

if __name__ == "__main__":
    start_time=time.time()
    path = './image_set/*.png'
    file_list = glob.glob(path)
    cnt = 0
    for i in file_list:        
        image = cv2.imread(i)
        name, extension = os.path.splitext(os.path.basename(i))
        
        #################################################################
       
        
        result = ['forward',0,0]
        
        #################################################################        
        
        if result[0][0] in name[-3:]:
            answer = '○'
            cnt += 1
        else:
            answer = '×'
        
        print(name, answer, result)       
        cv2.imshow('image', image)

        key = cv2.waitKey(200)

        if key == ord('q'):
            break
        
    
    cv2.destroyAllWindows()
    end_time = time.time()
    p_time = round(end_time-start_time,2)
    print('\nTotal:', str(len(file_list)))
    print('Acurracy:', str(round(100*cnt/len(file_list), 2))+" %")
    print('Processing Time:', str(p_time), 'FPS:', str(round(len(file_list)/p_time,3)))