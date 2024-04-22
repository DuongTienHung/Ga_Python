def f(n):
    if (n==1 or n==2):
        return 1
    else:
        return f(n-1)+f(n-2)
print(f(12))
n=int(input("nhap vao n: "))
for i in range(1,n+1,1):
    print(f(i),end=" ")


"""
n=3 hay la f(3)

=f(3-1)+f(3-2)
=f(2)+f(1)
=1+1
=2


f(4)
=f(4-1)+f(4-2)
=f(3)+f(2)
= 2 + 1
=3


"""