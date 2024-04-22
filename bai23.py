def Giaithua(n):
    if n==0:
        return 1
    else:
        return n*Giaithua(n-1)


a=Giaithua(8)
print(a)
# 8*7*6*5*4*3*2*1
"""
8*Giaithua(7)
8*7*Giaithua(7-1)
8*7*6*Giaithua(5)
8*7*6*5*Giaithua(4)
8*7*6*5*4*Giaithua(3)
8*7*6*5*4*3*Giaithua(2)
8*7*6*5*4*3*2*Giaithua(1)
8*7*6*5*4*3*2*1*Giaithua(0)
8*7*6*5*4*3*2*1*1


"""