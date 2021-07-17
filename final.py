# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 01:58:44 2021

@author: jdh38
"""


import numpy as np
import cv2


def mouse_event (event, x, y, flags, params) : #마우스 움직임 
    global x_init, y_init, drawing, human, human_sub, x_0, y_0, x_1, y_1, imgs, \
        img_num, img_size_x, img_size_y
    
    def update_pts () :
        params["top_left_pt"] = (min(x_init, x), min(y_init, y))
        
        params["bottom_right_pt"] = (max(x_init, x), max(y_init, y))
        
        
    if (event == cv2.EVENT_LBUTTONDOWN) :
        drawing = True
        x_init, y_init = x, y
        
        cv2.circle(human, (x_init, y_init), 2, (0, 255, 0), 3)
    
    elif ((event == cv2.EVENT_MOUSEMOVE) and (drawing)) :
        update_pts()
    
    elif (event == cv2.EVENT_LBUTTONUP) :
        drawing = False
        update_pts()
        
        (x_0, y_0), (x_1, y_1) = params["top_left_pt"], params["bottom_right_pt"]
        
        human = cv2.resize(human, (x_1-x_0, y_1-y_0))
        human = human_sub[y_0:y_1, x_0:x_1].copy()
        
        human = cv2.resize(human, (img_size_x, img_size_y))
        
        human_sub = human.copy()
        
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


def img_read() : #프레임을 읽어오는 함수
    global human, human_sub, cap, video, imgs, img_num
    
    if (video) :
        ret, human = cap.read()
        human = cv2.resize(human, (img_size_x, img_size_y))
        human_sub = human.copy()
    
    else :
        human = cv2.imread(imgs[img_num])
        human = cv2.resize(human, (img_size_x, img_size_y))
        human_sub = human.copy()


def onChange(pos):
    pass
    
def trackbar () : #프레임 관련 
    global ani_weighted, video
    ani_weighted = cv2.getTrackbarPos("a_weight %", "img") / 100
    video = cv2.getTrackbarPos('switch\nP V', "img")

fd = cv2.CascadeClassifier('opencv_haar/haarcascade_frontalface_alt.xml')

drawing = False
event_params = {"top_left_pt" : (-1, -1), "bottom_right_pt" : (-1, -1)}

cv2.namedWindow('img')
cv2.setMouseCallback('img', mouse_event, event_params)

cv2.createTrackbar('a_weight %', "img", 0, 100, onChange)
cv2.createTrackbar('switch\nP V', "img", 0, 1, onChange)

cv2.setTrackbarPos("a_weight %", "img", 100)
cv2.setTrackbarPos('switch\nP V', "img", 1)

cap = cv2.VideoCapture(0)

video = 1

sample_imgs = ['img/human1.jpg', 'img/human2.png', 'img/human3.jpg', 
        'img/family.jpg', 'img/tv_2person.jpg']

sample_img_num = 0
sample_img_num_range = 5

saved_imgs = []

saved_img_num = 0
saved_img_num_range = 0

cnt = 0

imgs = saved_imgs
img_num = saved_img_num
img_num_range = saved_img_num_range

ani_sel = 'original'

keys = {'Esc' : 27, 'N' : 110, 'P' : 112, '0번' : 48, '1번' : 49, '2번' : 50, 
        '3번' : 51, '4번' : 52, 'S' : 115, 'F' : 102, 'D' : 100}

k = keys['0번']

img_size_x = 600
img_size_y = 512

img_read()

font = cv2.FONT_HERSHEY_COMPLEX_SMALL

while (k != keys['Esc']) :
    
    trackbar()
    
    if video == False and imgs == [] :
        
        imgs = sample_imgs
        img_num = sample_img_num
        img_num_range = sample_img_num_range
        
        print("저장된 이미지가 없습니다. 샘플 이미지가 출력됩니다.")
        
        img_read()
        
    
   
    if (video) :
        
        if (k == keys['S']) :
            cv2.imwrite('img/saved_img' + str(cnt) + '.jpg', human)
            saved_imgs.append('img/saved_img' + str(cnt) + '.jpg')
            cnt += 1
            saved_img_num_range += 1
            
            img_num_range = saved_img_num_range
            
    
        img_read()
        
    else :
   
    
        if(k == keys['N']) :
            img_num += 1
            
            if (img_num >= img_num_range) :
                img_num = img_num_range - 1
                
            img_read()
            
        elif (k == keys['P']) :
            img_num -= 1
            
            if (img_num <= -1) :
                img_num = 0
                
            img_read()
            
        elif (k == keys['S']) :
            cv2.imwrite('img/saved_img' + str(cnt) + '.jpg', human)
            saved_imgs.append('img/saved_img' + str(cnt) + '.jpg')
            cnt += 1
            saved_img_num_range += 1
            
            img_num_range = saved_img_num_range
            
            if (imgs == sample_imgs) :
                img_num_range = sample_img_num_range
            
        elif (k == keys['D']) :
            imgs = sample_imgs
            img_num = sample_img_num
            img_num_range = sample_img_num_range
            
            img_read()
            
        elif (k == keys['F']) :
            if (saved_imgs != []) :
                
                imgs = saved_imgs
                img_num = saved_img_num
                img_num_range = saved_img_num_range
    
                img_read()
            
            else :
                print("저장된 이미지가 없습니다. 샘플 이미지가 출력됩니다.")
        
  
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        
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
        
      
    if (ani_sel != 'original') :  
        if(ani_sel == 'pig') :
            ani_inked = cv2.imread("img/pig_inked.jpg")
            
        elif (ani_sel == 'dog') :
            ani_inked = cv2.imread("img/dog_inked.jpg")
            
        elif (ani_sel == 'donkey') :
            ani_inked = cv2.imread("img/dng_inked.jpg")
            
        elif (ani_sel == 'panda') :
            ani_inked = cv2.imread("img/pnd_inked.jpg")
            
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

            ani_inked = cv2.resize(ani_inked, ((x2-x1),(y2-y1)))
        
            if (ani_sel == 'pig') :
               thre_start = 155
               
            elif (ani_sel == 'dog') :
               thre_start = 120
               
            elif (ani_sel == 'donkey') :
               thre_start = 40
               
            elif (ani_sel == 'panda') :
               thre_start = 20
            
            ani_ink_gray = cv2.cvtColor(ani_inked, cv2.COLOR_BGR2GRAY)
            aniMask_to_ani = cv2.threshold(ani_ink_gray, thre_start, 255, cv2.THRESH_BINARY)[1]
            
            
            
            ani_masked = cv2.bitwise_and(ani_inked, ani_inked, mask = aniMask_to_ani)
            
            human_cut = human[y1:y2, x1:x2]
            
            human_cut[ani_masked > 0] = human_cut[ani_masked > 0] * (1-ani_weighted) +\
                                        ani_masked[ani_masked > 0] * ani_weighted
                                        
            human.astype(np.uint8)
            
            human_sub = human.copy()
            
        
            
            
  
    cv2.imshow("img", human)
    
    if (video == False) :
        ani_sel = 'original'
    k = cv2.waitKey(20)
    
   
cap.release()
cv2.destroyAllWindows()

