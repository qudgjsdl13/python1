i=0
k=0
guguline=""

for i in range(2,10):
    guguline=guguline+(" #  %d단  #  "%i)

print(guguline)

for i in range(1,10):
    guguline=""
    for k in range(2,10):
        guguline=guguline+str("%2d X%2d = %2d"%(k,i,k*i))
    print(guguline)