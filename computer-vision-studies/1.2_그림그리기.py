import cv2

#1 다양한 선 그리기

img = cv2.imread('/Users/Danny/Desktop/GitHub/coding-academy-jioh/computer-vision-studies/white.png')

cv2.line(img, (50,50), (150,50), (255,0,0)) # B,G,R (R,G,B)

cv2.line(img, (200,50), (300,50), (0,255,0)) # B,G,R (R,G,B)

cv2.line(img, (350,50), (450,50), (0,0,255)) # B,G,R (R,G,B)

cv2.line(img, (50,70), (150,70), (0,0,255), 10) # B,G,R (R,G,B)

cv2.line(img, (100, 250), (400,300), (0,0,255), 20, cv2.LINE_4) # B,G,R (R,G,B)
cv2.line(img, (100, 300), (400,350), (0,0,255), 20, cv2.LINE_AA) # B,G,R (R,G,B)

cv2.imshow('lines', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

