import sys

input = sys.stdin.readline

N, M = map(int, input().split())
start = [list(map(int, input().rstrip())) for _ in range(N)]
goal = [list(map(int, input().rstrip())) for _ in range(N)]
answer = 0


def cnt3by3(arr, x, y):
    for i in range(3):
        for j in range(3):
            arr[x + i][y + j] = 1 - arr[x + i][y + j]


cnt = 0
for i in range(N - 2):
    for j in range(M - 2):
        if start[i][j] != goal[i][j]:
            cnt3by3(start, i, j)
            cnt += 1

if start == goal:
    print(cnt)
else:
    print(-1)
