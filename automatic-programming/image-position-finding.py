# imagePositionFinding = 0 # 변수 
# IMAGEPOSITIONFINDING = 0 # 상수

from matplotlib import image
import pyautogui as pg 

imageLocation = pg.locateCenterOnScreen('A_0.png', grayscale=True, confidence=0.5) # naver이미지가 있는 위치 가져옴
print(imageLocation)
pg.click(imageLocation)

