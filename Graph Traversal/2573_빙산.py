from collections import deque

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
time = 0

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        cx, cy = q.popleft()
        for d in range(4):
            nx = cx + dir[d][0]
            ny = cy + dir[d][1]

            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] != 0 and not visited[nx][ny]: #방문하지 않은 빙산이면
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                elif board[nx][ny] == 0: # 주변이 바다이면 개수 확인해야 함
                    visited[cx][cy] += 1


while True:
    cnt = 0 # 녹인 빙산 개수
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and board[i][j] != 0:
                bfs(i, j)
                cnt += 1

    # 주면 바다 개수 만큼 녹이기
    for i in range(N):
        for j in range(M):
            if visited[i][j] != 0:
                board[i][j] -= (visited[i][j] -1)
                if board[i][j] < 0:
                    board[i][j] = 0
    if cnt >= 2:
        print(time)
        break
    if cnt == 0:
        print(0)
        break

    time += 1
