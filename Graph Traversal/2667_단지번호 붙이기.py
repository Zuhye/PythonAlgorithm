import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().rstrip())) for _ in range(N)]
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[0] * N for _ in range(N)]
answer = []


def bfs(x, y):
    cnt = 1
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        a, b = q.popleft()

        for d in range(4):
            nx = a + dir[d][0]
            ny = b + dir[d][1]

            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = 1
                cnt += 1
                q.append((nx, ny))

    return cnt


for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and not visited[i][j]:
            cnt = bfs(i, j)
            answer.append(cnt)

answer.sort()
print(len(answer))
for i in answer:
    print(i)