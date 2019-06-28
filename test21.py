import random
num=[]

myList=[31,10,20]
print("현재 나의 리스트:%s"%myList)

myList.append(40)
print("append(40) 후의 리스트:%s"%myList)

print("pop()으로 추출한 값:%s"%myList.pop())
print("pop()후의 리스트:%s"%myList)

for i in range(0,10):
    num.append(random.randrange(0,10))
myList.sort()
print("sort() 후의 리스트:%s"%myList)
num.sort()
print(num)

myList.reverse()
print("reverse() 후의 리스트:%s"%myList)

print("20값의 위치:%d"%myList.index(20))

myList.insert(2,222)
print("insert2,222후의 리스트:%s"%myList)

myList.remove(222)
print("remove(222) 후의 리스트 :%s"%myList)

myList.extend([77,88,77])
print("extend([77,88,77])후의 리스트:%s"%myList)

print("77값의 개수:%d"%myList.count(77))

