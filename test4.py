a=int(input("정수를 입력하세요:"))
star="★"

for i in range(0,a,1):
    for j in range(0,i+1,1):
        print(star, end = "")
    print("")

for i in range(0,a,1):
    for j in range(a,i+1,-1):
        print(star, end = "")
    print("")