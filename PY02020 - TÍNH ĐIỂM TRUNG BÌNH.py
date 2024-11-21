n = int(input())

a = list(map(float, input().split()))
a.sort()
tmp = a[0]
while a.count(tmp) != 0: a.remove(tmp)
tmp = a[-1]
while a.count(tmp) != 0: a.pop()
print(round(sum(a) / len(a), 2))