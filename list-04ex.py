lst=[]
n=int(input("nhap vao so phan tu: "))
dem=0
while dem<n:
    dem=dem+1
    a=int(input("nhap vao phan tu: "))
    lst.append(a)
print("list ban vua nhap la: ",lst)

"""dem2=0
for i in lst:
    if i<5:
        dem2=dem2+1  #dem2=+1
print("so chu so nho hon 5 la:", dem2)"""

dem2=0
lst_index=[]
for j in range(len(lst)):
    if lst[j] <5:
        dem2+=1
        lst_index.append(j)
print(f"co {dem2} so nho hon 5 ")
print(f"cac vi tri index cua cac so nho hon 5 la: ", lst_index)

