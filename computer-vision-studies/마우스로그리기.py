import cv2

title = 'Mouse Event'
img = cv2.imread('white.png')
cv2.imshow(title, img)

colors = {
    'black':(0,0,0),
    'red':(0,0,255),
    'blue':(255,0,0),
    'green':(0,255,0)
}

# 1 = True, 0 = False
def onMouse(event, x, y, flags, params):
    print(event, x, y, flags, params)
    color = colors['black']
    if event == cv2.EVENT_LBUTTONDOWN: # 왼쪽 버튼을 누를경우
        # 컨트롤키와 쉬프트 키 모두 누른경우
        if flags & cv2.EVENT_FLAG_CTRLKEY and flags & cv2.EVENT_FLAG_SHIFTKEY:
            color = colors['green']
        elif flags & cv2.EVENT_FLAG_SHIFTKEY:
            color = colors['blue']
        elif flags & cv2.EVENT_FLAG_CTRLKEY:
            color = colors['red']

        cv2.circle(img, (x,y), 30, color, -1) # 지름이 30픽셀인 동그라미를 왼쪽 마우스를 눌렀을때 입력된 x, y좌표에 그려라
        cv2.imshow(title, img)

cv2.setMouseCallback(title, onMouse)

while True:
    if cv2.waitKey(0) & 0xFF == 27: # ESC 눌렀을때
        break

cv2.destroyAllWindows()