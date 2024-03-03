import sys

input = sys.stdin.readline

N = int(input())
score = [0] * 301
dp = [0] * 301

for i in range(N):
    score[i] = int(input())

dp[0], dp[1] = score[0], score[0] + score[1]
dp[2] = max(score[0] + score[2], score[1] + score[2])

for i in range(3, N):
    dp[i] = max(dp[i-2] + score[i], dp[i - 3]+score[i - 1] + score[i])


print(dp[N-1])