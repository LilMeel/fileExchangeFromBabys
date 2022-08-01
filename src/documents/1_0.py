n = int(input())
a = None
b = None
c = None
if n % 3 == 0:
    b = int(n/3)
    a = b-1 
    c = b+1
    print(a, b, c)
else:
    print(-1)