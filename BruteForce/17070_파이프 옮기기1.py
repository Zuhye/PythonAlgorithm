import sys

input = sys.stdin.readline

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]
#  dp[0][row][col]: 가로 파이프에 대한 dp
#  dp[1][row][col]: 대각선 파이프에 대한 dp
#  dp[2][row][col]: 세로 파이프에 대한 dp

dp[0][0][1] = 1  # (0,1)에 위치한 파이프

for i in range(2, N):
    if board[0][i] == 0:
        dp[0][0][i] = dp[0][0][i-1]

# (1, 1) 부터 계산 시작
for i in range(1, N):
    for j in range(1, N):
        # 가로, 세로
        if board[i][j] == 0:
            dp[0][i][j] = dp[0][i][j-1] + dp[1][i][j-1] # 그 전의 가로와 대각선 합
            dp[2][i][j] = dp[2][i-1][j] + dp[1][i-1][j] # 그 전의 세로와 대각선 합

        # 대각선 확인
        if board[i][j] == 0 and board[i][j-1] == 0 and board[i-1][j] == 0:
            dp[1][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]

result = dp[0][N-1][N-1] + dp[1][N-1][N-1] + dp[2][N-1][N-1]
print(result)