import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
adj = [[] for _ in range(N)]
for i in range(M):
    A, B = map(lambda x: x-1, map(int, input().split())) #A -=1 /B -=1
    adj[A].append(B)
    adj[B].append(A)

kevin = []
ans = (-1,10000)

def bfs(start, goal):
    chk = [False] * N
    chk[start] = True
    dq = deque()
    dq.append((start, 0))
    while dq: #dq가 비어있지 않다면 반복 실행
        now, d = dq.popleft()
        if now == goal:
            return d

        nd = d+1
        for nxt in adj[now]:
            if not chk[nxt]:
                chk[nxt] = True
                dq.append((nxt, nd))
            print(dq, nxt)

def get_kevin(start): #케빈 거리 (총 합)
    tot = 0
    for i in range(N):
        if i != start:
            tot += bfs(start, i) #0에서 1 + 0에서 2 + 0에서 3 + 0에서 4 = tot
    return tot

for i in range(N):
    kevin.append(get_kevin(i))

# print(f'kevin: {kevin}')

for i, v in enumerate(kevin): #index와 value를 같이 얻음
    if ans[1] > v:
        ans=(i, v)


print(ans[0]+1)