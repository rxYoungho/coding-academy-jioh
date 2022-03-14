"""
bool 자료형은 참(True)와 거짓(False)를 나타내는 자료형이다.

- True
- False

"""

a = True 
b = False 

print(type(a), type(b))

"""
"python" = 참
"" = 거짓 
[1,2,3] = 참
[] = 거짓
() = 거짓
{} = 거짓
1 = 참
0 = 거짓
None = 거짓
"""

a = [1,2,3,4]
while a: # while True
    print(a.pop())

secret = "1jdm@트쟏@Si2mdi"

print(bool(secret))