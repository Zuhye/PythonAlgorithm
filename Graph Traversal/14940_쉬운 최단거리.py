import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1

    while q:
        x, y = q.popleft()

        for d in range(4):
            dx = x + dir[d][0]
            dy = y + dir[d][1]
            if 0 <= dx < N and 0 <= dy < M and not visited[dx][dy]:
                if board[dx][dy] == 0:
                    visited[dx][dy] = 0
                elif board[dx][dy] == 1:
                    visited[dx][dy] = visited[x][y] + 1
                    q.append((dx, dy))


for i in range(N):
    for j in range(M):
        if board[i][j] == 2 and visited[i][j] == 0:
            bfs(i, j)


for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            print(0, end = ' ')
        else:
            print(visited[i][j]-1, end=' ')
    print()