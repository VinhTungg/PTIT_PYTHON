def cnt42(list):
    res = {num % 42 for num in list}
    return res

a = []
while len(a) < 10:
    line = input()
    numbers = list(map(int, line.split()))
    a.extend(numbers[:10 - len(a)])
res = cnt42(a)
print(len(res))