a="dienvien1;Jackychan;01/11/1970"
print(a)
arr=a.split(";")

print(arr)
print(type(arr))
for i in arr:
    print(i)

a2=",".join(arr)
print(a2)