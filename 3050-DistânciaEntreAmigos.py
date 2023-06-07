n = int(input())
p = [int(i) for i in input().split()]

dist = 0
k = -1
for i in range(n):
    d = p[0] + i + p[i]
    if d > dist:
        dist = d
        k = i

max_dist = 0
for j in range(n):
    if j != k:
        max_dist = max(max_dist, p[k] + abs(k - j) + p[j])

print(max_dist)
