import py
import pyautogui
import time

# Size of current display
# print(pyautogui.size())

# Current position of the mouse cursor
print(pyautogui.position())

# Mouse movement
# pyautogui.moveTo(100, 200) # x: 100, y: 200으로 이동하라
pyautogui.moveTo(24, 366, 2) # x: 100, y: 200으로 2초동안 이동하라 

# Mouse Click
pyautogui.click() # 기본적인 클릭
time.sleep(1) # 1초동안 시간을 멈춤

# Mouse 우측 Click
# pyautogui.click(button="right")

# Mouse Double Click
pyautogui.moveTo(389, 230, 2) # x: 100, y: 200으로 2초동안 이동하라 
pyautogui.doubleClick()

# Mouse Drag
# 816,81 -> 539, 80
pyautogui.moveTo(816, 200 ,2)
pyautogui.dragTo(539, 400, 2, button='left')

# Mouse Scroll
pyautogui.scroll(1) # Up
pyautogui.scroll(-2) # Down
pyautogui.scroll(-3, x = 50, y= 366) # Move to 50, 366, and scoll up 3 clicks



