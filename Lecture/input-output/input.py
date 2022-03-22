
# input의 사용

# a = input()
# print(a)

# 한줄에 결괏값 모두 출력하기
# for i in range(10):
#     print(i, end=',')

"""
 파일 열기모드
 w = 쓰기모드 - 파일에 내용을 쓸 때 사용
 r = 읽기모드 - 파일을 읽기만 할 때 사용
 a = 추가모드 - 파일의 마지막에 새로운 내용을 추가 시킬 때 사용
"""

# w
f = open("/Users/Danny/Desktop/GitHub/coding-academy-jioh/Lecture/input-output/NewFile.txt", 'w') 
for i in range(1,11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# r
f = open("/Users/Danny/Desktop/GitHub/coding-academy-jioh/Lecture/input-output/NewFile.txt", 'r')
# while True:
#     line = f.readline().strip()
#     if not line: break
    # print(line)
data = f.read()
print(data)
f.close()

# a
f = open("/Users/Danny/Desktop/GitHub/coding-academy-jioh/Lecture/input-output/NewFile.txt", 'a')
for i in range(11, 21):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()