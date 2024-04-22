lst=[]
n=int(input("nhap vao so phan tu: "))
dem=0
while dem<n:
    dem=dem+1
    a=int(input("nhap vao phan tu: "))
    lst.append(a)
print("list ban vua nhap la: ",lst)

#1 : tao list moi
lst_2=[]
for i in lst:
    lst_2.append(i**2)
print(lst_2)

#2:
dem2=0
for i in lst_2:
    if i>50:
        dem2+=1
print(f"list moi co {dem2} so lon hon 50")