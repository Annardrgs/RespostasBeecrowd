j = 0

while True:
    n = int(input())

    if n == 0:
        break

    i = l = k = m = 0
    j += 1

    i = n // 50
    k = (n - i * 50) // 10
    l = (n - (i * 50 + k * 10)) // 5
    m = (n - (i * 50 + k * 10 + l * 5)) // 1

    print("Teste", j)
    print(i, k, l, m)
    print()
