"""

다음은 "test.txt"라는 파일에 "Life is too short" 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램이다.

f1 = open("test.txt", 'w')
f1.write("Life is too short")

f2 = open("test.txt", 'r')
print(f2.read())

이 프로그램은 우리가 예상한 "Life is too short"라는 문장을 출력하지 않는다. 
우리가 예상한 값을 출력할 수 있도록 프로그램을 수정해 보자.

"""

"""
다음과 같은 내용을 지닌 파일 test.txt가 있다. 이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어서 저장해 보자.

Life is too short
you need java

"""

f = open('새파일.txt', 'r')
data = f.read()
f.close()

data = data.replace('java', 'python')

f = open('새파일.txt', 'w')
f.write(data)
f.close()