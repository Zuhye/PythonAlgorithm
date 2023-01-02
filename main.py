#11047 ,1449
import sys

input = sys.stdin.readline

coin = []
count = 0

N, K = map(int,input().split())
for i in range(N):
    coin.append(int(input()))
    # print(coin)

for i in coin[::-1]:
    if i <= K:
        max = K // i
        K = K - i*max
        count += 1*max
        # print(max ,K, count)
print(count)
