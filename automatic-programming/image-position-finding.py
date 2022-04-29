# imagePositionFinding = 0 # 변수 
# IMAGEPOSITIONFINDING = 0 # 상수

from matplotlib import image
import pyautogui as pg 

imageLocation = pg.locateCenterOnScreen('naver2.png') # naver이미지가 있는 위치 가져옴
pg.click(imageLocation)