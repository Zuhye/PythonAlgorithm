import sys


input = sys.stdin.readline

N, P = map(int, input().split())
stk = [[] for _ in range(7)]
cnt = 0

for _ in range(N):
    line, p = map(int, input().split())
    while stk[line] and stk[line][-1] > p :
        stk[line].pop()
        cnt += 1

    if stk[line] and stk[line][-1] == p:
        continue
    stk[line].append(p)
    cnt += 1
print(cnt)