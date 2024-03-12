import sys

input = sys.stdin.readline

N = int(input())
schedule = []
dp = [0 for _ in range(N+1)]
result = 0

for _ in range(N):
    t, p = map(int, input().split())
    schedule.append((t, p))


for i in range(N-1, -1, -1): # 퇴사 전날 부터 확인
    if (i + schedule[i][0]) <= N:
        dp[i] = max(result, schedule[i][1] + dp[i+schedule[i][0]])
        result = dp[i]
    else:
        dp[i] = result

print(result)
