import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [input() for _ in range(n)]
dp = [[0]*m for _ in range(n)]

for j in range(m):
    if board[0][j] == '1':
        dp[0][j] = 1

for i in range(1,n):
    if board[i][0]=='1':
        dp[i][0] = 1

    for j in range(1,m):
        if board[i][j] == '1':
            dp[i][j] = min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1]) +1
ans = 0
for i in range(n):
    for j in range(m):
        ans = max(ans, dp[i][j])

print(ans**2)