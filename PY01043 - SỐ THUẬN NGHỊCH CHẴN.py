from collections import deque

num = []

def check(n):
    if len(n) & 1: return False
    return n == n[::-1]

def init():
    queue = deque()
    for i in range(2, 10, 2):
        queue.append(i)
    while queue:
        tmp = queue.popleft()
        tmp = str(tmp)
        for i in range(0, 10, 2):
            m = tmp + str(i)
            if int(m) > 1000000: return False
            #print(m, end = ' ')
            if check(m): num.append(m)
            queue.append(m)

init()

for _ in range(int(input())):
    n = int(input())
    for i in num:
        if int(i) >= n: break
        print(i, end=' ')
    print()