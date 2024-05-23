import sys
from collections import deque

input = sys.stdin.readline

H, W = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs():
    q = deque()
    q.append((0, 0))
    visited = [[False] * W for _ in range(H)]
    cnt = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            dx = x + dir[i][0]
            dy = y + dir[i][1]

            if 0 <= dx < H and 0 <= dy < W:
                if board[dx][dy] == 0 and visited[dx][dy] == False:
                    visited[dx][dy] = True
                    q.append((dx, dy))
                elif board[dx][dy] == 1:
                    # 가장 자리 1들은 모두 0으로 변경하여 녹게 해야함
                    board[dx][dy] = 0
                    cnt += 1
                    visited[dx][dy] = True

    return cnt


result = []
time = 0

while True:
    count = bfs()
    result.append(count)

    if count == 0:  # count 가 0이면 모든 치즈가 녹음
        break
    time += 1

print(time)
print(result[-2])