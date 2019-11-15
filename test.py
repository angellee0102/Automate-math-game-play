import snp
import glob
import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
import pyautogui

images = glob.glob("pic/numbers/*.JPG")
img_array=[]
for img in images:
    image = cv2.imread (img)
    img_array.append (image)
region_equal=(100,270,750,400)

while True:
    equal = snp.locateOnScreen('pic\\equal.JPG',region=region_equal)
    answer_box=snp.locateOnScreen('pic\\answer_box.JPG',region=region_equal)
    if equal != None and answer_box!= None:
        # print('equal',equal)
        equal_list = list(equal)
        equal_x=equal_list[0]
        equal_y=equal_list[1]

        # print('answer_box',answer_box)
        answer_box_list = list(answer_box)
        answer_box_x=answer_box_list[0]
        answer_box_y=answer_box_list[1]
        
        # 左邊數字十位數
        region_left_number_left=(answer_box_x-120,answer_box_y+25,55,80)
        # 左邊數字個位數
        region_left_number_right=(answer_box_x-75,answer_box_y+25,55,80)
        is_left_number_two_digit=False
        left_digit=None
        for i in range(0,10):
            number_path='pic\\numbers\\'+str(i)+'.JPG'
            left_number_left_digit = snp.locateOnScreen(number_path,region=region_left_number_left,threshold=0.84)
            if left_number_left_digit!=None:
                is_left_number_two_digit=True
                left_digit=i
            left_number_right_digit = snp.locateOnScreen(number_path,region=region_left_number_right,threshold=0.84)
            if left_number_right_digit!=None:
                right_digit=i

        if is_left_number_two_digit==True: 
            left_number=left_digit*10+right_digit
            print('左邊數字',left_number)
        if is_left_number_two_digit==False:
            left_number=right_digit
            print('左邊數字:', left_number)


        # 中間數字
        region_middle_number=(equal_x-95,equal_y-20,60,100)
        for i in range(0,10):
            number_path='pic\\numbers\\'+str(i)+'.JPG'
            middle_digit = snp.locateOnScreen(number_path,region=region_middle_number,threshold=0.84)
            if middle_digit!=None:
                middle_number=i
                print('中間數字:',middle_number)
        
        # 右邊數字     
        region_right_number_left=(equal_x+85,equal_y-10,55,75)
        print(region_right_number_left)
        region_right_number_right=(equal_x+140,equal_y-10,55,75)
        print(region_right_number_right)
        is_right_number_two_digit=False
        right_left_digit=None
        for i in range(0,10):
            number_path='pic\\numbers\\'+str(i)+'.JPG'
            right_number_right_digit = snp.locateOnScreen(number_path,region=region_right_number_right,threshold=0.87)
            # 右邊的位元
            if right_number_right_digit!=None:
                is_right_number_two_digit=True
                right_right_digit=i
            right_nunmber_left_digit=snp.locateOnScreen(number_path,region=region_right_number_left,threshold=0.87)
            # 左邊的位元
            if right_nunmber_left_digit!=None:
                right_left_digit=i
        if is_right_number_two_digit==True: 
            print(right_left_digit,right_right_digit)
            right_number=right_left_digit*10+right_right_digit
            print('右邊數字',right_number)
        if is_right_number_two_digit==False:
            right_number=right_left_digit
            print('右邊數字:', right_number)

        # Calculation
        if (left_number/right_number==middle_number):# 除法
            pyautogui.click(answer_box_x+150,answer_box_y+270)
        elif(right_number/middle_number==left_number):# 乘法
            pyautogui.click(answer_box_x+270,answer_box_y+270)
        elif(right_number-middle_number==left_number):# 加號
            pyautogui.click(answer_box_x-150,answer_box_y+270)
        else:# 減號 
            pyautogui.click(answer_box_x,answer_box_y+270)
