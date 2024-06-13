for i in range (2,9):
    print(i) #2,3,4,5,6,7,8

for i in range (2,9,3):
    print(i) #2,5,8

count=0
while count<5:
    print(count)
    count=count+1 #0,1,2,3,4

count=0
while count<5:
    count=count+1
    print(count) #1,2,3,4,5

count=5
while count>0:
    count=count-1
    print(count) #5,4,3,2,1
else:
    print("waktu habis")

count=0
while True:
    print(count)
    count=count+1
    if count>10:
        break

count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

for i in range(20):
    if i%2==0:
        continue
    print(i)

for i in range(0, 5): #0,1,2,3,4
    for j in range(i):
        print("*")
    print() #nested loop



    # + - * / %

for i in range (0,10):
    if i%2==0:
        print("angka genap")
    else:
        print(i)




