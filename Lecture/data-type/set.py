"""
1. 리스트, 튜블, 딕셔너리등의 여러가지 데이터를 담는애들이 중복된 데이터를 원하지 않을때 SET을 씁니다.
"""

a = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,3,3,3,3,1,1,1,3,3]
print(set(a))
newSet = set(a)

# Add
newSet.add(4)
print(newSet)

# Update
newSet.update([1,2,3,4,5,6,7])
print(newSet)

# Remove
newSet.remove(6)
print(newSet)