import sys

input = sys.stdin.readline

T = int(input())


def dfs(x):
    visited[x] = 1
    next = arr[x]
    if not visited[next]:
        dfs(next)


for _ in range(T):
    cnt = 0
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [0] * (N + 1)

    for i in range(1, N + 1): # index가 정렬된 수랑 동일
        if not visited[i]:
            dfs(i)
            cnt += 1

    print(cnt)
