import array

def check(arr):
    for i in range(1, len(arr)):
        if (arr[i] ^ arr[i - 1]) & 1: return False
    return True

def func(arr):
    while check(arr):
        for i in range(1, len(arr)):
            if (arr[i] ^ arr[i - 1]) & 1: del a[i - 1:i + 1]

n = int(input())
