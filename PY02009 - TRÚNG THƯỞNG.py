from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = []
    for i in range(n):
        m = int(input())
        a.append(m)
    max_count = max(Counter(a).values())
    print(min(num for num, fre in Counter(a).items() if fre == max_count))