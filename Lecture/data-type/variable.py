a = 1
b = "python"
c = [1,2,3]



temp = [1,2,3,4] #temp: 04[3] 메모리를 가르키는 객체
print(id(temp)) # 140654946148608

b = temp 
print(id(b))

print(temp is b)
temp[1] = 5
print(temp, b)

'''
01 02 03 04
[] [] [] []
[] [] [] []
[] [] [] [[1,2,3,4]]
'''