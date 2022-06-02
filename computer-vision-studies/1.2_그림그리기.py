import cv2
import numpy as np
#1 다양한 선 그리기

img = cv2.imread('/Users/Danny/Desktop/GitHub/coding-academy-jioh/computer-vision-studies/white.png')

# cv2.line(img, (50,50), (150,50), (255,0,0)) # B,G,R (R,G,B)

# cv2.line(img, (200,50), (300,50), (0,255,0)) # B,G,R (R,G,B)

# cv2.line(img, (350,50), (450,50), (0,0,255)) # B,G,R (R,G,B)

# cv2.line(img, (50,70), (150,70), (0,0,255), 10) # B,G,R (R,G,B)

# cv2.line(img, (100, 250), (400,300), (0,0,255), 20, cv2.LINE_4) # B,G,R (R,G,B)
# cv2.line(img, (100, 300), (400,350), (0,0,255), 20, cv2.LINE_AA) # B,G,R (R,G,B)

# cv2.rectangle() -> 매개변수들: img, 좌표(x,y), 너비높이(w,h), 색(B,G,R), 두께(20)
#cv2.rectangle(img, (50,50), (150,150), (255,0,0))

# 번개 모양 좌표
pts1 = np.array([[50,50], [150,150], [100,140], [200,240]], dtype = np.int32)
pts2 = np.array([[350,250], [450,350], [400, 450], [300, 450], [250,350]], dtype = np.int32)

cv2.polylines(img, [pts1], False, (255,0,0), 1, cv2.LINE_AA)
cv2.polylines(img, [pts2], True, (0,0,0), 1, cv2.LINE_AA)


cv2.imshow('polygons', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

