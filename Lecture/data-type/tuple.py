"""
리스트는 []로 둘러싸지만 튜플은 ()으로 둘러싼다.
리스트는 값의 생성, 삭제, 수정이 가능하지만 튜플은 절대로 그 값을 바꿀 수 없다.
"""

t1 = ()
t2 = (1,)
t3 = (1,2,3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab','cd'))

# 튜플의 요소값을 지우거나 변경하려고 하면 어떻게 될까?
t1 = (1,2,'a','b')
# del t1[0] #TypeError: 'tuple' object doesn't support item deletion
# t1[0] = 'c' # TypeError: 'tuple' object does not support item assignment

# 인덱싱하기
t1 = (1,2,'a','b')
print(t1[0], t1[-1])

# 슬라이싱하기
print(t1[1:3])

# 튜플 더하기
t1 = (1, 2, 'a', 'b')
t2 = (3,4)
print(t1 + t2) #(1, 2, 'a', 'b', 3, 4)

# 튜플 곱하기
t2 = (3,4)
print(t2*4) #(3, 4, 3, 4, 3, 4, 3, 4)

# 튜플 길이 구하기
t1 = (1,2,'a','b')
print(len(t1))

