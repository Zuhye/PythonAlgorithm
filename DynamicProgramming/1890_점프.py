import sys


input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):

        if i == N-1 and j == N-1:
            print(dp[i][j])

        value = board[i][j]

        if i + value < N:
            dp[i+value][j] += dp[i][j]
        if j + value < N:
            dp[i][j+value] += dp[i][j]