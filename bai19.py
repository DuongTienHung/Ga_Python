def PTB1(a,b): # ax+b=0
    if a==0 and b==0:
        return "Vo so nghiem"
    elif a==0 and b!=0:
        return " Vo nghiem"
    else:
        return "x={}" .format(-b/a)

b=PTB1(5,6)
print(b)
print(type(b))
