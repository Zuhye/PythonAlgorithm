import sys
from collections import deque

input = sys.stdin.readline

w, h = map(int, input().split())
board = [list(input().rstrip()) for _ in range(w)]
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited = [[0] * h for _ in range(w)]
    visited[x][y] = 1
    cnt = 0

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dir[d][0]
            ny = y + dir[d][1]

            if nx < 0 or nx >= w or ny < 0 or ny >= h:
                continue
            elif board[nx][ny] == "L" and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    cnt = max(cnt, visited[nx][ny])
                    q.append((nx, ny))

    return cnt-1


result = 0
for i in range(w):
    for j in range(h):
        if board[i][j] == 'L':
            result = max(result, bfs(i, j))


print(result)