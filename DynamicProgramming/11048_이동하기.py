import sys

input = sys.stdin.readline

N, M = map(int, input().split()) # N: 세로 / M: 가로
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * M for _ in range(N)]
dp[0][0] = board[0][0]

for i in range(1, M):  # 위쪽 테두리
    dp[0][i] = dp[0][i-1] + board[0][i]

for i in range(1, N):  # 왼쪽 테두리
    dp[i][0] = dp[i-1][0] + board[i][0]


for i in range(1, N):
    for j in range(1, M):
        dp[i][j] = max(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + board[i][j]


print(dp[N-1][M-1])