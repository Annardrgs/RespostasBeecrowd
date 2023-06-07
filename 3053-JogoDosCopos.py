n = int(input())
pos = input()

while n > 0:
    troca = int(input())
    
    if troca == 1 and (pos == 'A' or pos == 'B'):
        pos = 'B' if pos == 'A' else 'A'
    elif troca == 2 and (pos == 'B' or pos == 'C'):
        pos = 'C' if pos == 'B' else 'B'
    elif troca == 3 and (pos == 'A' or pos == 'C'):
        pos = 'C' if pos == 'A' else 'A'
    
    n -= 1

print(pos)
