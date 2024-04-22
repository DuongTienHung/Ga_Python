a="abcdefghijklmnopqrstuvwxyz"
b="zxcvbnmasdfghjklqwertyuiop"


n=input("nhap vao ky tu a-z de ma hoa: ")
s=""
for i in n:
    index=a.find(i)
    s=s+b[index]
print(s)
