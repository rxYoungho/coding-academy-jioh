"""
믹서기 
- input: 딸기, 우유, 얼을, 설탕 
- output: 딸기 쉐이크

코딩할때 함수 왜쓰나요? 
- 반복을 줄이기 위해
- 일목요연하게 보여주기 위해 

용어 정리
- parameter: 매개변수는 받을때
- argument: 인자는 부를때
- return: 결과값

def 함수명(매개변수):
    <수행 문장 1>
    <수행 문장 2>
    ...
    

"""

def mixer(strawberry, milk, ice, sugar): # 매게변수를 받는다
    return 'Strawberry Shake'

# 함수
def add(a,b):
    return a + b

# 리턴값이 없는 함수
def minus(a,b):
    print(a-b)

minus(900,12) # 인수 argument

# 매개 변수가 없는 함수
def say():
    return "I Love you"

print(say())

# 매개변수 지정
result = mixer(sugar=900, milk=1000, strawberry='True', ice="100g")
print(result)

# 매개변수 몇개 받아야 할 지 모를때 쓰는 함수
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

print(add_many(1,2,3,4,5,6,7,8,9,10,11,2,3,5,6,1,2,3,5,6,2))

# *args랑 그냥 섞어서 쓸때
def add_mul(choice, *args):
    if choice == 'add':
        result = 0
        for i in args:
            result = result + i
        return result
    elif choice == 'mul':
        result = 1
        for i in args:
            result = result * i
        return result

print(add_mul('mul', 5,4,2,4,6,2,3,1,23,3,5,2))
