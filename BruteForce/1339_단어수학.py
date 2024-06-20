import sys

input = sys.stdin.readline

N = int(input())
numbers = [input().strip() for _ in range(N)]
find = dict()
answer = 0

for i in numbers:
    length = len(i)
    for j in i:
        if j not in find:
            find[j] = 10 ** (length - 1)
        else:
            find[j] += 10 ** (length - 1)
        length -= 1
result = sorted(find.values(), reverse=True)

number = 9
for i in result:
    answer += i * number
    number -= 1

print(answer)
