import sys
from collections import deque
import copy

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
cnt = [0] * 101
max_floor = 0
min_floor = 100
dir = ((-1, 0), (1, 0), (0, -1), (0, 1))

for i in board:
    max_floor = max(max_floor, max(i))
    min_floor = min(min_floor, min(i))


def bfs(i, j):
    global count
    q = deque()
    q.append((i, j))
    count += 1
    temp[i][j] = "#"

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dir[d][0]
            ny = y + dir[d][1]

            if 0 <= nx < N and 0 <= ny < N and temp[nx][ny] != "#":
                q.append((nx, ny))
                temp[nx][ny] = "#"


for floor in range(min_floor, max_floor + 1):
    count = 0
    temp = copy.deepcopy(board)
    for i in range(N):
        for j in range(N):
            if temp[i][j] < floor:
                temp[i][j] = "#"
    for i in range(N):
        for j in range(N):
            if temp[i][j] != "#":
                bfs(i, j)

    cnt[floor] = count

print(max(cnt))