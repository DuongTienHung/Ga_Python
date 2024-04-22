def N_trai(n):
    for i in range(n):
        for j in range(n):
            if j==0 or j==n-1 or i==j:
                print("*",end="  ")
            else:
                print(" ",end="  ")
        print()

def N_phai(n):
    for i in range(n):
        for j in range(n):
            if j==0 or j==n-1 or i+j==n-1:
                print("*",end="  ")
            else:
                print(" ",end="  ")
        print()

n=int(input("nhap n di thim: "))
if n%2==0:
    N_trai(n)
else:
    N_phai(n)
