import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
r1, c1, r2, c2 = map(int, input().split())
dir = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]
visited = [[0] * N for _ in range(N)]


def bfs(i, j):
    q = deque()
    q.append((i, j))

    while q:
        x, y = q.popleft()

        if x == r2 and y == c2:
            return visited[x][y]

        for d in range(6):
            nx = x + dir[d][0]
            ny = y + dir[d][1]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    return -1


print(bfs(r1, c1))

