import sys
from itertools import permutations

input = sys.stdin.readline

A, B = map(str, input().split())
numsA = list("".join(i) for i in permutations(A))
answer = -1

for i in numsA:
    if i[0] == '0':
        continue
    if int(i) < int(B):
        answer = max(answer, int(i))

print(answer)
