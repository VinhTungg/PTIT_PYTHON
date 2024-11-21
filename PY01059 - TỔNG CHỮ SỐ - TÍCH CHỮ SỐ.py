def solve(n):
    chan = 0
    le = 1
    cnt = 0
    cnt0 = 0
    for i in range(len(n)):
        if i & 1:
            le *= int(n[i]) if n[i] != '0' else 1
            cnt += 1
            if n[i] == '0': cnt0 += 1
        else:
            chan += int(n[i])
    le = le if cnt != cnt0 else 0
    return chan, le

for _ in range(int(input())):
    n = input()
    chan, le = solve(n)
    print(chan, le)