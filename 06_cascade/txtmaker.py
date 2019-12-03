import cv2
import glob
import os
import itertools as it

def multiple_file_types(*patterns):
    return it.chain.from_iterable(glob.iglob(pattern) for pattern in patterns)

types = ('*.png', '*.jpg')
images = []

positives_image_dir_name = 'positive' 
negatives_image_dir_name = 'negative'
size = 40
positives_txt = open('positives.txt', 'w')
negatives_txt = open('negatives.txt', 'w')

for pos in multiple_file_types(os.path.join(positives_image_dir_name,'*.jpg'), os.path.join(positives_image_dir_name,'*.png')):
    name = os.path.abspath(pos)
    raw = cv2.imread(pos)
    resized= cv2.resize(raw, (size, size), interpolation = cv2.INTER_AREA)
    cv2.imwrite(pos, resized)
    positives_txt.write(name+' 1 0 0 '+str(size)+' ' +str(size)+'\n')

for neg in multiple_file_types(os.path.join(negatives_image_dir_name,'*.jpg'), os.path.join(negatives_image_dir_name,'*.png')):
    name = os.path.abspath(neg)
    negatives_txt.write(name+'\n')

positives_txt.close()
negatives_txt.close()    