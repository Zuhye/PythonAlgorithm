# 첫째 줄에 사람의 수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄에는 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어진다. (1 ≤ Pi ≤ 1,000)

N = int(input())
time = list(map(int, input().split()))

time.sort()

result = 0
for i in range(1, N+1):
    result += sum(time[0:i])

print(result)
