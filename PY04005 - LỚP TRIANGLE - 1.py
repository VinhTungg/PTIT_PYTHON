from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

results = []

for _ in range(int(input())):
    ans = input().split()
    P1 = Point(float(ans[0]), float(ans[1]))
    P2 = Point(float(ans[2]), float(ans[3]))
    P3 = Point(float(ans[4]), float(ans[5]))
    Dist1 = P1.distance(P2)
    Dist2 = P2.distance(P3)
    Dist3 = P3.distance(P1)
    if max([Dist1, Dist2, Dist3]) * 2 < Dist1 + Dist2 + Dist3:
        results.append("{:.3f}".format(Dist1 + Dist2 + Dist3))
    else:
        results.append('INVALID')

for result in results:
    print(result)
