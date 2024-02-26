import sys
from math import comb

input = sys.stdin.readline

while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        break

    result = comb(n, k)
    print(result)
