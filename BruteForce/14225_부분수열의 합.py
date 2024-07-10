import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
max_value = sum(arr)
numbers = [0] * (max_value + 1)  # [0, 1, 2, 3, 4, 5, 6, 7, 8]
numbers[0] = 1

for i in range(len(arr)):
    result = list(combinations(arr, i + 1))
    for comb in result:
        numbers[sum(comb)] = 1

if 0 in numbers:
    for idx in range(max_value+1):
        if numbers[idx] == 0:
            print(idx)
            break
else:
    print(max_value+1)


# 다른 사람 코드

arr.sort()
target = 0

for i in arr:
    if target + 1 < i:
        break
    target += i

print(target + 1)
