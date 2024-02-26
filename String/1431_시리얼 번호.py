import sys

input = sys.stdin.readline

N = int(input())
numbers = [input().rstrip() for _ in range(N)]


def numbers_sum(number):
    total = 0
    for i in number:
        if i.isdigit():
            total += int(i)
    return total


numbers.sort(key=lambda x: (len(x), numbers_sum(x), x))
for i in numbers:
    print(i)
