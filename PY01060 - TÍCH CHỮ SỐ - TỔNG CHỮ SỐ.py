def solve(n):
    chan = 0
    le = 1
    for i in range(len(n)):
        if i % 2 == 0:
            le *= int(n[i]) if n[i] != '0' else 1
        else:
            chan += int(n[i])
    return chan, le

for _ in range(int(input())):
    n = input()
    chan, le = solve(n)
    print(le, chan)