from cmath import log

t = int(input())
while t:
    n, x, m = map(float, input().split())
    ans = (m / n)
    ans = log(ans).real / log(1 + x / 100).real
    print(int(ans + 1))
    t -= 1