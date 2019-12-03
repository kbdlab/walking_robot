import cv2
import numpy as np

'''한글 주석은 라즈베리 파이 상에서 유니코드 에러가 발생하므로 해당 상황에서는 모두 지우고 사용할 것!'''

def detect(cascade_classifier, image):
        # 실제로 학습에 사용되는 것은 흑백 이미지
        # 필요 시 색 에 관련한 조건문을 추가할 수도 있음
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # 기본값은 아래와 같이 no object.
        mode="No object"
        
        # scale Factor : 1 초과의 값, 1에 가까울 수록 연산량이 많아짐
        # minNeighbors : 0에 가까울수록 더 많은 물체를 잡음 (더 많이 틀림)
        # minSize : 최소 크기 - 너무 먼 물체를 잡는 문제를 해결하기 위함
        cascade_obj = cascade_classifier.detectMultiScale(
            gray_image,
            scaleFactor=1.02,
            minNeighbors=5,
            minSize=(16,16),           
        )
        
        # 잡힌 물체들 목록이  cascade_obj'
        # 이 예제에서는 굳이 40, 40 이상을 따로 구분해서 표시함
        # 16~40 사이의 물체는 인식은 되는데 그려주지는 않음. 단지 width height를 확인하는 용도
        # 크기를 체크하면서 최적 값을 찾는 흔적으로 보임.
        for (x_pos, y_pos, width, height) in cascade_obj:
            # draw a rectangle around the objects
            #print(width,height)
            if(width>=40):
                cv2.rectangle(image, (x_pos, y_pos), (x_pos+width, y_pos+height), (255, 255, 255), 2)
                cv2.putText(image, 'Stop', (x_pos, y_pos-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                mode="Stop"
        return mode
    
        # 아래와 같이 x,y,z,h 좌표를 리턴하여 나중에 그릴 수도 있음.
        '''for (x_pos, y_pos, width, height) in cascade_obj:
            if width >= 40:            
                x, y, w, h = x_pos, y_pos, x_pos+width, y_pos+height
                mode = "stop"
        return (mode, x, y, w, h)'''
       
    
'''학습한 xml 파일 필요'''
'''
        
# 이미지 스트리밍 시
image = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
obj = cv2.CascadeClassifier('stopsign.xml')
mode = detect(obj, image)  

# V-rep 에서
temp = cv2.imread(path)
image = temp
mode = detect(obj, image)  

# 라즈베리 파이에서
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array

    obj = cv2.CascadeClassifier('stopsign.xml')
    mode = detect(obj, image)  




        