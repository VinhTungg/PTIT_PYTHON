for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n - 2):
        l = i + 1
        r = n - 1
        tmp = a[i]
        while l < r:
            if tmp + a[l] + a[r] == 0:
                ans += 1
                l += 1
            elif tmp + a[l] + a[r] < 0: l += 1
            else: r -= 1
    print(ans)