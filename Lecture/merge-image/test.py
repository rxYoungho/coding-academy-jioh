

"""
<법례>
[] = 어쩌꼬를 의미합니다.
{} = 어쩌고를 의미합니다.
=====================
!시작!
=====================

A [P] R {I} {L}

"""

userInput = input()
temp=""
answer = "APRIL"

for char in userInput:
    if char == 'P':
        a = f"[{char}]"
        temp+=a
    if char == 'I' or char == 'L':
        b = f"({char})"
        temp+=b
print(temp)