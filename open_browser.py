import snp
import glob
import os
import cv2

import numpy as np
import pyautogui

pyautogui.hotkey('win','r')
pyautogui.typewrite('microsoft-edge:https://gamekuo.com/html5/3963_math-genius-games')
pyautogui.PAUSE = 1
pyautogui.press('enter')
pyautogui.PAUSE = 3

pyautogui.moveTo(400,300)
pyautogui.scroll(-300)