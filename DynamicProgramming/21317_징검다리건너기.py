import sys

input = sys.stdin.readline

N = int(input())
energy = []
dp = [1e9] * N
dp[0] = 0

for i in range(N - 1):
    small, big = map(int, input().split())
    energy.append((small, big))

K = int(input())

# 작은 에너지, 큰 에너지만 고려
if N == 1:
    print(0)
    exit()
elif N == 2:
    print(energy[0][0])
    exit()

dp[1] = energy[0][0]
dp[2] = min(energy[0][1], energy[0][0] + energy[1][0])

for i in range(3, N):
    dp[i] = min(dp[i-1] + energy[i-1][0], dp[i-2] + energy[i-2][1])

dp2 = dp[:]  # K 고려하기 위해 새로운 dp 복사
result = dp[-1]

for i in range(N-3):
    if dp[i] + K < dp[i+3]:
        dp2[i+3] = dp[i] + K

        for j in range(i + 4, N): # 위에서 갱신이 됐으니 다시 최소값 추출
            dp2[j] = min(dp[j], dp2[j-1] + energy[j-1][0], dp2[j-2] + energy[j-2][1])

        result = min(dp2[-1],result)

print(result)