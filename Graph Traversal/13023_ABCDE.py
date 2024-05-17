import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
relation = [[] for _ in range(N)]
visited = [False for _ in range(N)]
answer = False

for i in range(M):
    a, b = map(int, input().split())
    relation[a].append(b)
    relation[b].append(a)


def dfs(idx, cnt):
    global answer
    if cnt == 4:
        answer = True
        return

    for j in relation[idx]:
        if not visited[j]:
            visited[j] = True
            dfs(j, cnt + 1)
            visited[j] = False


for i in range(N):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False

    if answer:
        break

if answer:
    print(1)
else:
    print(0)