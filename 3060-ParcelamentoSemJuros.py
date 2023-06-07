v = int(input())
p = int(input())

if v % p == 0:
    x = v // p
    for _ in range(p):
        print(x)
else:
    x = v % p
    y = v // p
    for _ in range(x):
        print(y + 1)
    for _ in range(p - x):
        print(y)
