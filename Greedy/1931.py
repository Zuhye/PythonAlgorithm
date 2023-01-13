# 첫째 줄에 회의의 수 N(1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N+1 줄까지 각 회의의 정보가 주어지는데
# 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다.
# 시작 시간과 끝나는 시간은 231-1보다 작거나 같은 자연수 또는 0이다.

N = int(input())
time = [[0]*2 for _ in range(N)]
result = 0
endTime = 0

for i in range(N):
    start, end = (map(int, input().split()))
    time[i][0] = start
    time[i][1] = end
time.sort(key=lambda x: (x[1], x[0]))

for start, end in time:
    if start >= endTime:
        result += 1
        endTime = end
print(result)