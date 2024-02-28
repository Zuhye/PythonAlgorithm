import sys
from collections import deque

input = sys.stdin.readline

V = int(input())
E = int(input())
board = [[] for _ in range(V + 1)]
visited = [False] * (V + 1)
answer = 0

for i in range(E):
    s, e = map(int, input().split())
    board[s].append(e)
    board[e].append(s)


def bfs(v, answer):
    q = deque([v])
    visited[v] = True

    while q:
        x = q.popleft()
        for i in board[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                answer += 1

    print(answer)

bfs(1, answer)
