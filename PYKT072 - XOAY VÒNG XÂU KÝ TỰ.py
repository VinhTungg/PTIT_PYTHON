import os
a = []
for _ in range(int(input())):
    a.append(input())

ans, ok = 1e9, 1

for i in a:
    step = 0
    for j in a:
        if j == i: continue
        else:
            take = 0
            tmp = j
            while tmp != i and take <= len(i):
                tmp = tmp[1:] + tmp[0]
                step += 1
                take += 1
            if take > len(i):
                ok = 0
    ans = min(ans, step)

print(ans if ans != 1e9 and ok == 1 else -1)