 -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 13:45:34 2019

@author: SHF_W
"""

import random
from datetime import datetime

def run():
    out = ''
    try:
        for i in range(10):
            try:
                x = random.randint(-7,7)    
                direction = x / abs(x)
                print(i, direction)
            except Exception as e:
                out += str(i)+' '+str(e)+'\n'
    finally:
        print('\n')
        print(out)

def rsp(shape):
    allowed = ['가위','바위', '보']
    if shape not in allowed:
        raise ValueError
    print(shape)   

def run2():
    try:
        rsp('가위')
        rsp('바위')
        rsp('보자기')
    except ValueError:
        print('잘못된 입력입니다.')
        
def run3():
    timestamp = datetime.now().strftime('%y%b%d%H%M%S')
    print(timestamp)

for frame in ... : 
    ....
    if key == ord('s'):
        timestamp = datetime.now().strftime('%y%b%d%H%M%S')
        image_name = 'image_'+timestamp+'.png'

import os # 위에 추가

image_num=0
directory = './data_'+datetime.now().strftime('%y%b%d%H%M%S')
for frame in ... :
    ....
    if key == ord('s'):
        image_name = 'image_'+str(image_num)+'.png'
        image_num += 1
        try:
            os.makedirs(directory)
        except OSError:
            pass
        path = os.path.join(directory, image_name)
        cv2.imwrite(path, image)
        