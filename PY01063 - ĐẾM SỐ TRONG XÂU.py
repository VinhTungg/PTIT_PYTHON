for _ in range(int(input())):
    s = input()
    n = input()
    cnt = 0
    m = 0
    for i in range(len(s) - len(n) + 1):
        if i >= m:
            tmp = s[i:i + len(n)]
            if tmp == n:
                cnt += 1
                m = i + len(n)
    print(cnt)