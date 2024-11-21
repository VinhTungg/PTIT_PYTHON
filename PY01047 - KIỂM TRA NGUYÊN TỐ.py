import math
def check(n):
    m = int(n)
    for i in range(2, int(math.sqrt(m)) + 1):
        if m % i == 0:
            return False
    return m > 2

for _ in range(int(input())):
    s = input()
    s = s[max(0, len(s) - 4):]
    print("YES" if check(s) else "NO")