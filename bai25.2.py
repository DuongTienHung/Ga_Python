t="123456789"
print(t[0],t[-1])
#cach khac
print(len(t))
for i in range(len(t)):
    if i==0 or i==len(t)-1:
        print(t[i],end=" ")
