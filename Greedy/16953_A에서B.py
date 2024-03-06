import sys

input = sys.stdin.readline

A, B = map(int, input().split())
result = 0

while B != A:

    if B % 10 == 1:
        B = int(B//10)
        result += 1
    elif B % 2 == 0 and B != 0:
        B //= 2
        result += 1
    else:
        print(-1)
        exit()

print(result+1)