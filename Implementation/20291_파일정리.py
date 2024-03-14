import sys

input = sys.stdin.readline

N = int(input())
files = []
extension = {}

for i in range(N):
    n, h = map(str, input().split('.'))
    files.append(n)
    if h.rstrip() not in extension:
        extension[h.rstrip()] = 1

    else:
        extension[h.rstrip()] += 1

result = sorted(extension.items())

for i in result:
    print(*i)