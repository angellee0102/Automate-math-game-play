# import pyautogui
# pyautogui.PAUSE = 1
# pyautogui.hotkey('win','r')
# # pyautogui.press('shift') # 如果會卡中文輸入法，請記得切換，可去除開頭 #
# pyautogui.typewrite('cmd')
# pyautogui.press('enter')
# # pyautogui.press('shift') # 如果會卡中文輸入法，請記得切換，可去除開頭 #
# pyautogui.typewrite('echo Hello World!',0)
# pyautogui.press('enter')

import snp
import pyautogui
import glob
import os
import cv2

# open browser and website
pyautogui.hotkey('win','r')
pyautogui.typewrite('microsoft-edge:https://gamekuo.com/html5/3963_math-genius-games')
pyautogui.PAUSE = 1
pyautogui.press('enter')
pyautogui.PAUSE = 10
pyautogui.PAUSE = 5
pyautogui.keyDown('alt')
pyautogui.press(' ')
pyautogui.press('x')
pyautogui.keyUp('alt')
pyautogui.scroll(-300)
pyautogui.PAUSE = 10

region=(100,160,800,800)
# skip video ad
p = snp.locateOnScreen('pic\skipAd_button.JPG')
if p != None:
    print('found skipAd_button')
    pyautogui.click(p[0]+p[2]//2,p[1]+p[3]//2)

# click play
play_button = snp.locateOnScreen('pic\play_button.JPG', region=region)
p=play_button
if p != None:
    print('found play_button')
    pyautogui.click(p[0]+p[2]//2,p[1]+p[3]//2)


equal = snp.locateOnScreen('pic\equal.JPG',region=region)
p=equal
if p != None:
    print('equal',p)
    pyautogui.click(p[0]+p[2]//2,p[1]+p[3]//2)

images = glob.glob("pic/numbers/*.JPG")
img_array=[]
for img in images:
    image = cv2.imread (img)
    img_array.append (image)

print(img_array)