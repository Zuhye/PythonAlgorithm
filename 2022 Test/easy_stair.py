import sys
input = sys.stdin.readline

N = int(input())
MOD = 1_000_000_000
# dp[n][d]: 길이가 n, 마지막 숫자가 d인 계단 수 개수
dp = [[0]*10 for _ in range(101)] # d:0~9까지이므로 10 / n: 100까지 이므로 101

for j in range(1, 10):
    dp[1][j] = 1

for i in range(2, 101):
    for j in range(10):
        if j > 0:
            dp[i][j] += dp[i-1][j-1]
            dp[i][j] %= MOD
        if j < 9:
            dp[i][j] += dp[i-1][j+1]
            dp[i][j] %= MOD

print(sum(dp[N])%MOD)