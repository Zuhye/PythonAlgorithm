from itertools import combinations
import sys

input = sys.stdin.readline

while True:
    numbers = list(map(int, input().split()))
    if numbers[0] == 0:
        exit()

    for i in combinations(numbers[1:], 6):
        print(*i)

    print()