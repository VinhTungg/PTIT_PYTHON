#MLE

def find_three_numbers(a):
    num1 = 1e18
    num2 = 1e18
    num3 = 1e18
    for num in a:
        if num < num1:
            num3 = num2
            num2 = num1
            num1 = num
        elif num < num2:
            num3 = num2
            num2 = num
        elif num < num3:
            num3 = num
    return [num1, num2, num3]

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(sum(find_three_numbers(a)))