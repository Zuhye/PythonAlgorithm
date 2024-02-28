import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())
board = [[False] * (N + 1) for _ in range(N + 1)]
visited1 = [False] * (N + 1)
visited2 = [False] * (N + 1)

for i in range(M):
    s, e = map(int, input().split())
    board[s][e] = True
    board[e][s] = True


def dfs(v):
    visited1[v] = True
    print(v, end=' ')
    for i in range(N + 1):
        if not visited1[i] and board[v][i]:
            dfs(i)


def bfs(v):
    q = deque([v])
    visited2[v] = True

    while q:
        x = q.popleft()
        print(x, end=' ')
        for i in range(1, N + 1):
            if not visited2[i] and board[x][i]:
                q.append(i)
                visited2[i] = True


dfs(V)
print()
bfs(V)
