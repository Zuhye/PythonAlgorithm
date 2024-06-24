import sys

input = sys.stdin.readline

M, N = map(int, input().split())  # M: 세로 / N: 가로

# 범위체크를 생략하기 위해 둘러쌈
board = [[0] * (N + 2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(M)] + [[0] * (N + 2)]
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dp = [[-1] * (N + 2) for _ in range(M + 2)]
dp[1][1] = 1


def dfs(x, y):
    if dp[x][y] == -1:  # 첫 방문이라면
        dp[x][y] = 0

        for d in range(4):
            nx = x + dir[d][0]
            ny = y + dir[d][1]

            if board[nx][ny] > board[x][y]:
                dp[x][y] += dfs(nx, ny)  # 조건에 맞는 네방향 경로수 누적
    return dp[x][y]


print(dfs(M, N))
