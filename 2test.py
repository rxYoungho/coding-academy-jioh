import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread("/Users/Danny/Desktop/GitHub/coding-academy-jioh/black.jpg")
img = cv2.resize(img, (0,0), fx=0.2,fy=0.2,interpolation=cv2.INTER_AREA)
# 이진 이미지로 변환
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
# 잡음 제거
kernel = np.ones((3,3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
# 이미지 확장을 통해 확실한 배경 요소 확보
sure_bg = cv2.dilate(opening, kernel, iterations=3)
# distance transform을 적용하면 중심으로 부터 Skeleton Image를 얻을 수 있음.
# 이 결과에 Threshold를 적용하여 확실한 객체 또는 전경 요소를 확보
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 3)
ret, sure_fg = cv2.threshold(dist_transform, 0.5*dist_transform.max(), 255, 0)
sure_fg = np.uint8(sure_fg)
# 배경과 전경을 제외한 영역 곳을 확보
unknown = cv2.subtract(sure_bg, sure_fg)
# 마커 생성 작성
ret, markers = cv2.connectedComponents(sure_fg)
markers = markers + 1
markers[unknown == 255] = 0
# 앞서 생성한 마커를 이용해 Watershed 알고리즘을 적용
markers = cv2.watershed(img, markers)
img[markers == -1] = [255,0,0]
images = [gray,thresh,opening, sure_bg, dist_transform, sure_fg, unknown, markers, img]
titles = ['Gray', 'Binary', 'Opening', 'Sure BG', 'Distance', 'Sure FG', 'Unknow', 'Markers', 'Result']
for i in range(len(images)):
    plt.subplot(3,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()