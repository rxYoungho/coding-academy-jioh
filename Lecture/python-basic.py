"""
Compiler: 코드를 작성하고 실행하였을때 코드를 검사한다. -> C
Interpreter: 코드를 작성함과 동시에 코드를 검사한다. -> Python

Python :: 고대 신화의 나오는 파르나소스 산의 동굴에 살던 큰 뱀 

구글: 50% 코드는 파이썬입니다.
인스타그램: 파이썬
드롭박스: 파이썬

파이썬의 장점
1. 협업이 편하다
2. 유지 보수가 편하다.

개발자들의 꿈의 직장
    네카라쿠배당(네이버, 카카오, 라인, 쿠팡, 배달의민족, 당근마켓)
    FANG(Facebook, Amazon, Netflix, Google)

파이썬으로 할 수 있는것들
- 웹/앱
- 게임
- 인공지능/머신러닝
- 다양한 프로젝트
- 데이터베이스

"""


# 파이썬은 인간다운 언어이다
if 4 in [1,2,3,4]: print("4가 있습니다.")
# 만약 4가 1,2,3,4 중에 있으면 "4 가 있습니다."를 출력한다.

# 파이썬은 개발 속도가 빠르다! 
a = 1 # int
b = "a" # char -> string
c = "abc" # string
d = 2.0 # float (double)

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# 조건문
a = 3 
if a > 1: 
    print("a is greater than 1")

# for
for a in [1,2,3]:
    print(a)

for i in range(0,5):
    print(i) # 0,1,2,3,4,

# while
i = 0
while i < 3:
    i = i + 1
    print(i)

# 함수
def add(a, b):
    return a + b

print(add(4,5))


"""

*****
****
***
**
*

"""