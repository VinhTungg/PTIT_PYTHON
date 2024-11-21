from collections import Counter

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    count = Counter(arr)
    max_cnt = max(count.values())
    if max_cnt > n // 2:
        ans = min(num for num, fre in count.items() if fre > n // 2)
        print(ans)
    else: print("NO")