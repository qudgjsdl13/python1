i=0
hap=0

num=int(input("숫자를 입력하세요:"))

for i in range(1,num+1,1):
    hap=hap+i

print("1에서 %d까지의 합: %d" %(num,hap))