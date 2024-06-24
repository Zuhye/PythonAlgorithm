import sys
from itertools import product

input = sys.stdin.readline

n, m = map(int, input().split())  # n: 크기 / m: 친구 수
board = [list(map(int, input().split())) for _ in range(n)]
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
friend = []
routes = []
answer = 0

for i in range(m):
    x, y = map(int, input().split())
    friend.append([x - 1, y - 1])


def dfs(x, y, path, count):
    if count == 4:
        temp.append(list(path))
        return

    for d in range(4):
        nx = x + dir[d][0]
        ny = y + dir[d][1]

        if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in path:
            path.append((nx, ny))
            dfs(nx, ny, path, count + 1)
            path.pop()  # 백트래킹: 경로에서 제거


def total(arr):
    value = 0
    visited = set()
    for route in arr:
        for x, y in route:
            if (x, y) not in visited:
                visited.add((x, y))
                value += board[x][y]
    return value


# 모든 친구들의 경로 탐색
for x, y in friend:
    temp = []
    dfs(x, y, [(x, y)], 1)
    routes.append(temp)

answer = 0
for comb in product(*routes):
    answer = max(answer, total(comb))

print(answer)
