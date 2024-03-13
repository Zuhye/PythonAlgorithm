import sys

input = sys.stdin.readline

N = int(input())
date = [0] * 366

for _ in range(N):
    s, e = map(int, input().split())
    for i in range(s, e+1):
        date[i] += 1


col = 0
row = 0
result = 0
for i in range(len(date)):
    if date[i] != 0:
        row += 1
        col = max(col, date[i])
    else:
        result += col * row
        row = 0
        col = 0
result += col * row
print(result)