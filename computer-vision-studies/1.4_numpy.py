import cv2
import numpy as np 

# img = cv2.imread("/Users/Danny/Desktop/GitHub/coding-academy-jioh/computer-vision-studies/white.png")
# print(type(img)) # numpy.ndarray 형태
# print(img.ndim) # n-dimensional?
# print(img.shape) # (1278, 2184, 3) = (h, w, n-dim) 
# print(img.size) # 8373456 -> 1278 * 2184 * 3


# # 0 ~ 255 -> 음수 또는 소수점이 없고 최대크기가 255이므로 uint8을 데이터 타입으로 사용하여 2의 8승 / 8비트
# print(img.dtype) # uint8
# print(img.itemsize) # 각 요소의 크기가 1바이트 임을 알리는 것 -> 8비트

# numpy 배열 생성
# a = np.array([1,2,3,4])
# print(a)
# print(a.dtype) # int64 
# print(a.shape) # (4,1,1)

# print("*"*30)
# b = np.array([[1,2,3,4], [5,6,7,8], [1,1,1,1]])
# print(b)
# print(b.shape) # 4,3

# print("*"*30)
# c = np.array([1,2,3.14,4])
# print(c) # float64
# print(c.dtype)

# d = np.array([1,2,3,4], dtype=np.float32)
# print(d)

# 임의로 타입을 정해줄때
# a = np.uint8([1,2,3,4])

# 크기와 초기 값으로 numpy array 생성
# a = np.empty((2,3)) # 쓰레기값으로 배열 생성 // 2 rows, 3 cols 2열 3행 
# print(a)
# print(a.dtype) # float64

# a.fill(255)
# print(a)

# b = np.zeros((2,3))
# print(b)
# print(b.dtype)

# c = np.zeros((2,3), dtype=np.int8)
# print(c)
# print(c.dtype)

# """
# uint8 vs. int8
 
#  unsigned integer (음수가 없는 정수 = 양수만 취급함) = 256개 

#  int8 (음수, 양수 둘 다 포함) 512개
# """

# d = np.ones((2,3))
# print(d)

# e = np.full((2,2,2,1,1), 255) # 3차원 배열 (row, 1개 row기준 dimension, col), n-dimension
# print(e)


# 기존 image를 사용하여 같은 shape을 갖는 np array 만들기
img = cv2.imread('/Users/Danny/Desktop/GitHub/coding-academy-jioh/computer-vision-studies/white.png')
print(img.shape)

a = np.empty_like(img)
b = np.zeros_like(img)
c = np.ones_like(img)
d = np.full_like(img, 220)

print(a)
print(b)
print(c)
print(d)

