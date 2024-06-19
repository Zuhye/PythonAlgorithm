import sys

input = sys.stdin.readline

N, C = map(int, input().split())
wifi = list(int(input()) for _ in range(N))
wifi.sort()

start = 1
end = wifi[-1] - wifi[0]
answer = 0

while start <= end:
    mid = (start + end) // 2
    cur = wifi[0]
    cnt = 1

    for i in range(1, len(wifi)):
        if wifi[i] >= cur + mid:
            cnt += 1
            cur = wifi[i]

    if cnt >= C:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)