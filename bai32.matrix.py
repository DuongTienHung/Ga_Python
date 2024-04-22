from random import randrange

arr=[]
row=4
column=3
for i in range(row):
    onerow=[]
    for j in range(column):
        onerow.append(randrange(0,21))
    arr.append(onerow)
print(arr)


for i in range(len(arr)):
    for j in range(len(arr[i])):
       print(arr[i][j],end="\t")
    print()
print(arr[1][2])