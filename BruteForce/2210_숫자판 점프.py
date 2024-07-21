import sys

input = sys.stdin.readline

board = [list(map(str, input().split())) for _ in range(5)]
results = set()
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(x, y, arr):
    if len(arr) == 6:
        results.add(arr)
        return
    for d in range(4):
        nx = x + dir[d][0]
        ny = y + dir[d][1]

        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, arr + board[nx][ny])


for i in range(5):
    for j in range(5):
        dfs(i, j, board[i][j])

print(len(results))