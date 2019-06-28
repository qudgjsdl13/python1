# numList=[]
#
# for num in range(1,6):
#     numList.append(num)
# print(numList)
#
# numList1=[num for num in range(1,6)]
# print(numList1)

# oldList=["짜장면","탕수육","군만두"]
# newList=oldList
# print(newList)
# oldList[0]="짬뽕"
# oldList.append("깐풍기")
# print(newList)

oldList=["짜장면","탕수육","군만두"]
newList=oldList[:]
print(newList)
oldList[0]="짬뽕"
oldList.append("깐풍기")
print(newList)
print(oldList)