n=input("nhap vao 1 chuoi can tach: " )
s1=""
s2=""
for i in n:
    if i.isalpha():
        s1=s1+i  #s1+=i
    elif i.isdigit():
        s2=s2+i
print("day so la:", s2 )
print("day chu la:", s1 )