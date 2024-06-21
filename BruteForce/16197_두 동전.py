import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())   # N: 세로 / M: 가로
board = [list(input().rstrip()) for _ in range(N)]
coins = deque()
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
temp = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 'o':
            temp.extend((i, j))
coins = deque([(temp[0], temp[1], temp[2], temp[3], 0)])

while coins:
    x1, y1, x2, y2, cnt = coins.popleft()

    if cnt >= 10:
        print(-1)
        exit(0)

    for d in range(4):
        nx1 = x1 + dir[d][0]
        ny1 = y1 + dir[d][1]
        nx2 = x2 + dir[d][0]
        ny2 = y2 + dir[d][1]

        if 0 <= nx1 < N and 0 <= ny1 < M and 0 <= nx2 < N and 0 <= ny2 < M:

            # 벽인 경우
            if board[nx1][ny1] == '#':
                nx1, ny1 = x1, y1
            if board[nx2][ny2] == '#':
                nx2, ny2 = x2, y2
            coins.append((nx1, ny1, nx2, ny2, cnt + 1))

        elif 0 <= nx1 < N and 0 <= ny1 < M: # 두번째 코인이 떨어진 경우
            print(cnt + 1)
            exit(0)
        elif 0 <= nx2 < N and 0 <= ny2 < M: # 첫번째 코인이 떨어진 경우
            print(cnt + 1)
            exit(0)

