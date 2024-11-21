t = int(input())
while t:
    s = input()
    res = set()
    num = 0
    for i in s:
        if i.isdigit():
            num = num * 10 + int(i)
        else: num = 0
    print(min(res))
    t -= 1