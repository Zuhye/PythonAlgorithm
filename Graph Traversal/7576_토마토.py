import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())  # M: 가로 N: 세로
board = [list(map(int, input().split())) for _ in range(N)]
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
tomato = []
answer = 0

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            tomato.append((i, j))

tomato = deque(tomato)

while tomato:
    a, b = tomato.popleft()

    for d in range(4):
        nx = a + dir[d][0]
        ny = b + dir[d][1]

        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
            board[nx][ny] = board[a][b] + 1
            tomato.append((nx, ny))

for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            print(-1)
            exit()
        if answer < board[i][j]:
            answer = board[i][j]

print(answer-1)