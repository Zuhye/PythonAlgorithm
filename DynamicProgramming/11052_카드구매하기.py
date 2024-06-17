import sys

input = sys.stdin.readline

N = int(input())
cardpack = list(map(int, input().split()))
dp = [0] * (N+1)

dp[1] = cardpack[0] # 1인 경우
dp[2] = max(cardpack[1], dp[1] + cardpack[0]) # 2인 경우 (그냥 2 값이랑, 1+1 중 큰 값)


for i in range(3, N+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j] + cardpack[j-1])

print(dp[N])