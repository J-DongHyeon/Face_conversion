# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 01:58:44 2021

@author: jdh38
"""


import numpy as np
import cv2

#윈도우에 마우스 이벤트가 발생했을 때 실행되는 함수 (이미지 모드에서만 동작하는 함수)
def mouse_event (event, x, y, flags, params) : 
    global x_init, y_init, drawing, human, human_sub, x_0, y_0, x_1, y_1, imgs, \
        img_num, img_size_x, img_size_y
    
    #윈도우에 사용자가 표시한 사각형의 좌표를 최신화 하는 함수
    def update_pts () :
        params["top_left_pt"] = (min(x_init, x), min(y_init, y))
        
        params["bottom_right_pt"] = (max(x_init, x), max(y_init, y))
        
    #마우스 왼쪽버튼 클릭 시
    if (event == cv2.EVENT_LBUTTONDOWN) :
        drawing = True
        x_init, y_init = x, y
        
        cv2.circle(human, (x_init, y_init), 2, (0, 255, 0), 3)
    
    #마우스 왼쪽 버튼을 클릭한 상태로 움직이고 있을 때
    elif ((event == cv2.EVENT_MOUSEMOVE) and (drawing)) :
        update_pts()
    
    #마우스 왼쪽 버튼을 땐 경우 (사용자가 드래그한 사각형의 크기에 맞게 이미지를 확대)
    elif (event == cv2.EVENT_LBUTTONUP) :
        drawing = False
        update_pts()
        
        (x_0, y_0), (x_1, y_1) = params["top_left_pt"], params["bottom_right_pt"]
        
        human = cv2.resize(human, (x_1-x_0, y_1-y_0))
        human = human_sub[y_0:y_1, x_0:x_1].copy()
        
        human = cv2.resize(human, (img_size_x, img_size_y))
        
        human_sub = human.copy()
        
    #마우스 오른쪽 버튼을 땐 경우 (이미지 축소)
    elif (event == cv2.EVENT_RBUTTONUP) :
            
        human_sub = cv2.imread(imgs[img_num])
        human_sub = cv2.resize(human_sub, (img_size_x, img_size_y))
        
        x_rear = int((img_size_x + x_1) / 2)
        x_front = int(x_0 / 2)
        y_rear = int((img_size_y + y_1) / 2)
        y_front = int(y_0 / 2)
        
        human = cv2.resize(human, (x_rear - x_front, y_rear - y_front))
        human = human_sub[y_front : y_rear, x_front : x_rear].copy()
        
        human = cv2.resize(human, (img_size_x, img_size_y))
        
        human_sub = human.copy()
        
        x_0 = x_front; y_0 = y_front; x_1 = x_rear; y_1 = y_rear

#프레임을 읽어오는 함수
def img_read() :
    global human, human_sub, cap, video, imgs, img_num
    
    if (video) :
        ret, human = cap.read()
        human = cv2.resize(human, (img_size_x, img_size_y))
        human_sub = human.copy()
    
    else :
        human = cv2.imread(imgs[img_num])
        human = cv2.resize(human, (img_size_x, img_size_y))
        human_sub = human.copy()

#트랙바 값이 변할 때 실행되는 함수
def onChange(pos):
    pass
    
#트랙바의 현재 값을 가져오는 함수
def trackbar () :  
    global ani_weighted, video
    ani_weighted = cv2.getTrackbarPos("a_weight %", 'Face Conversion') / 100
    video = cv2.getTrackbarPos('switch\nP V', 'Face Conversion')

if (__name__ == '__main__') :
    #얼굴 검출 모델
    fd = cv2.CascadeClassifier('../docs/opencv_haar/haarcascade_frontalface_alt.xml')
    
    #사용자가 윈도우에 사각형을 그릴 때 좌표를 담을 변수
    drawing = False
    event_params = {"top_left_pt" : (-1, -1), "bottom_right_pt" : (-1, -1)}
    
    #'Face Conversion' 이름의 윈도우에 마우스 콜백함수와 트랙바 생성
    cv2.namedWindow('Face Conversion')
    cv2.setMouseCallback('Face Conversion', mouse_event, event_params)
    
    cv2.createTrackbar('a_weight %', 'Face Conversion', 0, 100, onChange)
    cv2.createTrackbar('switch\nP V', 'Face Conversion', 0, 1, onChange)
    cv2.setTrackbarPos("a_weight %", 'Face Conversion', 100)
    cv2.setTrackbarPos('switch\nP V', 'Face Conversion', 1)
    
    #노트북 카메라로 실시간 영상 보여줌
    cap = cv2.VideoCapture(0)
    
    video = 1
    
    #샘플 이미지들의 경로
    sample_imgs = ['../docs/Imgs/human1.jpg', '../docs/Imgs/human2.png', '../docs/Imgs/human3.jpg', 
            '../docs/Imgs/family.jpg', '../docs/Imgs/tv_2person.jpg']
    
    #현재 샘플 이미지 인덱스와 총 개수
    sample_img_num = 0
    sample_img_num_range = 5
    
    #사용자가 저장한 이미지 경로를 담을 리스트
    saved_imgs = []
    
    #저장된 이미지의 인덱스와 총 개수
    saved_img_num = 0
    saved_img_num_range = 0
    
    cnt = 0
    
    imgs = saved_imgs
    img_num = saved_img_num
    img_num_range = saved_img_num_range
    
    #현재 선택된 동물 탈을 의미하는 변수
    ani_sel = 'original'
    
    #각 단축키들의 아스키 코드를 담은 딕셔너리
    keys = {'Esc' : 27, 'N' : 110, 'P' : 112, '0번' : 48, '1번' : 49, '2번' : 50, 
            '3번' : 51, '4번' : 52, 'S' : 115, 'F' : 102, 'D' : 100}
    
    k = keys['0번']
    
    #이미지 크기
    img_size_x = 600
    img_size_y = 512
    
    img_read()
    
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    
    #윈도우가 종료되지 않는 한 무한 반복
    while (k != keys['Esc']) :
        
        trackbar()
        
        #이미지 모드 이면서 저장된 이미지가 현재 없는 경우, 샘플 이미지 출력
        if video == False and imgs == [] :
            
            imgs = sample_imgs
            img_num = sample_img_num
            img_num_range = sample_img_num_range
            
            print("저장된 이미지가 없습니다. 샘플 이미지가 출력됩니다.")
            
            img_read()
            
        
        #비디오 모드인 경우, 실시간 영상 출력
        if (video) :
            
            #'S' 키를 눌러 현재 이미지를 저장하는 경우
            if (k == keys['S']) :
                cv2.imwrite('../docs/Imgs/saved_img' + str(cnt) + '.jpg', human)
                saved_imgs.append('../docs/Imgs/saved_img' + str(cnt) + '.jpg')
                cnt += 1
                saved_img_num_range += 1
                
                img_num_range = saved_img_num_range
                
        
            img_read()
       
        #이미지 모드인 경우
        else :
            #'N'키를 눌러 다음 이미지로 넘어가는 경우
            if(k == keys['N']) :
                img_num += 1
                
                if (img_num >= img_num_range) :
                    img_num = img_num_range - 1
                    
                img_read()
                
            #'P'키를 눌러 이전 이미지로 넘어가는 경우    
            elif (k == keys['P']) :
                img_num -= 1
                
                if (img_num <= -1) :
                    img_num = 0
                    
                img_read()
                
            #'S' 키를 눌러 현재 이미지를 저장하는 경우
            elif (k == keys['S']) :
                cv2.imwrite('../docs/Imgs/saved_img' + str(cnt) + '.jpg', human)
                saved_imgs.append('../docs/Imgs/saved_img' + str(cnt) + '.jpg')
                cnt += 1
                saved_img_num_range += 1
                
                img_num_range = saved_img_num_range
                
                if (imgs == sample_imgs) :
                    img_num_range = sample_img_num_range
                
            #'D' 키를 눌러 샘플 이미지를 출력하는 경우
            elif (k == keys['D']) :
                imgs = sample_imgs
                img_num = sample_img_num
                img_num_range = sample_img_num_range
                
                img_read()
                
            #'F' 키를 눌러 저장된 이미지를 출력하는 경우
            elif (k == keys['F']) :
                if (saved_imgs != []) :
                    
                    imgs = saved_imgs
                    img_num = saved_img_num
                    img_num_range = saved_img_num_range
        
                    img_read()
                
                else :
                    print("저장된 이미지가 없습니다. 샘플 이미지가 출력됩니다.")
            
      
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
            
        #윈도우에 단축키 표시 (이미지 모드인 경우 추가 단축키 있음)
        if (video == False) :
            cv2.putText(human, 'N : next, P : past', (10, 75), font, 1, (200, 0, 0), 2)
            cv2.putText(human, 'F : saved image, D : sample image', (10, 95), font, 1, \
                        (200, 0, 0), 2)
            cv2.putText(human, 'Mouse Drag : Zoom in, Zoom out', (10, 115), font, 1,\
                        (200, 0, 0), 2)
            
        
        cv2.putText(human, 'S : save', (180, 55), font, 1, (200, 0, 0), 2)
            
        cv2.putText(human, '0 : Original', (10, 15), font, 1, (200, 0, 0), 2)
        
        cv2.putText(human, '1 : Pig, 2 : Dog, 3 : Donkey, 4 : Panda', (10, 35), font, 
                    1, (200, 0, 0),2)
        
        cv2.putText(human, 'Esc : End', (10, 500), font, 1, (200, 0, 0), 2)
    
        
        #각 단축키를 눌렀을 때의 기능
        if (k == keys['0번']) :  
            ani_sel = 'original'
            img_read()
            
        elif(k == keys['1번']) :
            ani_sel = 'pig'
            img_read()
            
        elif (k == keys['2번']) :
            ani_sel = 'dog'
            img_read()
            
        elif (k == keys['3번']) :
            ani_sel = 'donkey'
            img_read()
            
        elif (k == keys['4번']) :
            ani_sel = 'panda'
            img_read()
            
        #동물 이미지를 가져오는 부분
        if (ani_sel != 'original') :  
            if(ani_sel == 'pig') :
                ani_inked = cv2.imread("../docs/Imgs/pig_inked.jpg")
                
            elif (ani_sel == 'dog') :
                ani_inked = cv2.imread("../docs/Imgs/dog_inked.jpg")
                
            elif (ani_sel == 'donkey') :
                ani_inked = cv2.imread("../docs/Imgs/dng_inked.jpg")
                
            elif (ani_sel == 'panda') :
                ani_inked = cv2.imread("../docs/Imgs/pnd_inked.jpg")
                
            #얼굴 검출 모델을 이용하여 원본 이미지에서 얼굴 인식 후 사각형 좌표 반환
            frects = fd.detectMultiScale(human, scaleFactor = 1.3, minNeighbors = 4)
            
            
            for (x, y, w, h) in frects :
          
                x1 = x
                y1 = y
                x2 = x + w
                y2 = y + h
                
                x1 = x1 - 10
                x2 = x2 + 20
                y1 = y1 - 60
                y2 = y2 + 10
    
                #동물 이미지의 크기를 인식된 얼굴 크기에 맞춤
                ani_inked = cv2.resize(ani_inked, ((x2-x1),(y2-y1)))
            
                if (ani_sel == 'pig') :
                   thre_start = 155
                   
                elif (ani_sel == 'dog') :
                   thre_start = 120
                   
                elif (ani_sel == 'donkey') :
                   thre_start = 40
                   
                elif (ani_sel == 'panda') :
                   thre_start = 20
                
                #동물 이미지를 흑백 모델로 변환 후, threshold함수를 이용하여 완전히 이진화
                #시킴으로써 마스크를 구한다.
                ani_ink_gray = cv2.cvtColor(ani_inked, cv2.COLOR_BGR2GRAY)
                aniMask_to_ani = cv2.threshold(ani_ink_gray, thre_start, 255, cv2.THRESH_BINARY)[1]
                
                #동물 이미지에 마스크를 적용하여 깔끔하게 만든다.
                ani_masked = cv2.bitwise_and(ani_inked, ani_inked, mask = aniMask_to_ani)
                
                human_cut = human[y1:y2, x1:x2]
                
                #투명도에 따라 동물 이미지의 비중을 조정한다.
                human_cut[ani_masked > 0] = human_cut[ani_masked > 0] * (1-ani_weighted) +\
                                            ani_masked[ani_masked > 0] * ani_weighted
                                            
                human.astype(np.uint8)
                
                human_sub = human.copy()
    
        #사람 이미지를 윈도우에 나타낸다.
        cv2.imshow('Face Conversion', human)
        
        #비디오 모드에서 이미지 모드로 변환 시 'ani_sel'을 초기화 한다.
        if (video == False) :
            ani_sel = 'original'
        
        #윈도우에 어떠한 키 입력이 되는지 20ms 주기로 확인한다.
        k = cv2.waitKey(20)
        
    #ESC 키가 눌리면 윈도우를 종료한다.
    cap.release()
    cv2.destroyAllWindows()
    
