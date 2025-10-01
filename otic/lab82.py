import random

N = int(input("???")) # кількість рядків

for i in range(N):
    s = input("??? ")
    k = len(s) // 3
    parts = [s[:k], s[k:2*k], s[2*k:]]
    random.shuffle(parts)
    
    print("".join(parts))