import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
max_v = 0
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(x, y, cnt, result):
    global max_v
    if cnt == 4:
        if max_v < result:
            max_v = result
    else:
        for d in range(4):
            dx = x + dir[d][0]
            dy = y + dir[d][1]

            if 0 <= dx < N and 0 <= dy < M and not visited[dx][dy]:
                visited[dx][dy] = 1
                dfs(dx, dy, cnt + 1, result + board[dx][dy])
                visited[dx][dy] = 0


def o(x, y):  # ㅗ 모양 탐색
    global max_v
    for d in range(4):
        tmp = board[x][y]
        for k in range(3):
            t = (d + k) % 4
            dx = x + dir[t][0]
            dy = y + dir[t][1]

            if 0 <= dx < N and 0 <= dy < M:
                tmp += board[dx][dy]
        if max_v < tmp:
            max_v = tmp


for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 1, board[i][j])
        o(i, j)
        visited[i][j] = 0

print(max_v)
