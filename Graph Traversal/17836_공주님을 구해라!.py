import sys
from collections import deque

input = sys.stdin.readline

N, M, A = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(i, j):
    visited[i][j] = 1
    q = deque()
    q.append((i, j))
    gram_time = 10001

    while q:
        x, y = q.popleft()

        if (x, y) == (N - 1, M - 1):
            return min(visited[x][y] - 1, gram_time)

        if board[x][y] == 2:
            gram_time = visited[x][y]-1 + N-1-x + M-1-y

        for d in range(4):
            nx = x + dir[d][0]
            ny = y + dir[d][1]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if board[nx][ny] == 0 or board[nx][ny] == 2:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
    return gram_time


answer = bfs(0, 0)
if answer <= A:
    print(answer)
else:
    print("Fail")
