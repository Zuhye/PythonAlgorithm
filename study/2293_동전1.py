import sys

input = sys.stdin.readline

n, k = map(int, input().split())  # n: 동전 개수 / k: 원하는 값
coins = [int(input()) for _ in range(n)]
coins.sort()
dp = [0] * (k + 1)  # dp[1]: 1원 만드는 개수 , .., dp[k]: k원 만드는 개수
dp[0] = 1

for coin in coins:
    for i in range(coin, k + 1):
        dp[i] += dp[i - coin]  # 동전 5일때, dp[6]을 구하는 방법은 dp[1]의 방법을 추가
print(dp[k])
