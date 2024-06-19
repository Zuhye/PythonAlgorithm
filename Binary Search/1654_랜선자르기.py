import sys

input = sys.stdin.readline

K, N = map(int, input().split())
cable = [int(input()) for _ in range(K)]
cable.sort()

start = 1
end = cable[-1]
answer = 0

while start <= end:
    cnt = 0
    mid = (start + end) // 2

    for i in range(K):
        cur = cable[i]
        while cur >= mid:
            cur -= mid
            cnt += 1

    if cnt >= N:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)