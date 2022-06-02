import matplotlib.pyplot as plt 
import numpy as np 

# a = np.array([2, 6, 7, 3, 12, 8, 4, 5])
# plt.plot(a)
# plt.show()

# x = np.arange(10) # 0 ~ 9
# y = x ** 2
# plt.plot(x, y)
# plt.show()

# 3. Plot의 색을 지정하기
# x = np.arange(10) # 0 ~ 9
# y = x ** 2
# plt.plot(x, y, 'c') # b, g, r, c(cyan 청록색), m(Magenta 자홍색) ,y(yellow), k(black), w(white)
# plt.show()

"""
- : 실선 
-. : 점 이음선
. : 점
o : 원
^ : 정삼각형
> : 우 삼각형
2 : 작은 정삼각형
4 : 작은 우 삼각형
p : 오각형
h : 육각형
D : 다이아몬드 표
-- : 이음선
: : 점선
, : 픽셀
v : 역삼각형
< : 좌 삼각형
1 : 작은 역삼각형
3 : 작은 좌 삼각형
s : 사각형
* : 별표
+ : 더하기 표
x : 엑스 표
"""

# x = np.arange(10)
# f1 = x + 5
# f2 = x ** 2
# f3 = x **2 + x*2

# plt.plot(x, 'r--') # 빨간색 이음선
# plt.plot(f1, 'g.') # 초록색 점 
# plt.plot(f2, 'bv') # 파란색 역삼각형
# plt.plot(f3, 'ks') # 검은색 사각형
# plt.show()

# x = np.arange(10)
# plt.subplot(2, 2, 1) # 2행 2열 중 첫번째 그리드
# plt.plot(x, x**2)

# plt.subplot(2, 2, 2) # 2행 2열 중 두번째 그리드
# plt.plot(x, x*5)

# plt.subplot(2, 2, 3) 
# plt.plot(x, np.sin(x))

# plt.subplot(2, 2, 4) 
# plt.plot(x, np.cos(x))

# plt.show()

# 4. 이미지 표시
import cv2 
# img = cv2.imread('/Users/Danny/Desktop/GitHub/coding-academy-jioh/computer-vision-studies/에스파윈터/에스파윈터1.jpg')
# plt.imshow(img[:,:,::-1])
# plt.xticks([])
# plt.yticks([])
# plt.show()

img1 = cv2.imread('/Users/Danny/Desktop/GitHub/coding-academy-jioh/computer-vision-studies/에스파윈터/에스파윈터1.jpg')
img2 = cv2.imread('/Users/Danny/Desktop/GitHub/coding-academy-jioh/computer-vision-studies/에스파윈터/에스파윈터2.jpg')
img3 = cv2.imread('/Users/Danny/Desktop/GitHub/coding-academy-jioh/computer-vision-studies/에스파윈터/에스파윈터3.jpg')

plt.subplot(1,3,1)
plt.imshow(img1[:,:,::-1])



plt.subplot(1,3,2)
plt.imshow(img2[:,:,::-1])



plt.subplot(1,3,3)
plt.imshow(img3[:,:,::-1])
plt.show()