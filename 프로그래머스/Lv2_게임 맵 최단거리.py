from collections import deque


def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[0] * m for _ in range(n)]

    answer = 0

    def bfs(x, y):
        q = deque()
        q.append((x, y))
        visited[x][y] = 1

        while q:
            x, y = q.popleft()

            for d in range(4):
                dx = x + dir[d][0]
                dy = y + dir[d][1]

                if 0 <= dx < n and 0 <= dy < m and maps[dx][dy] == 1 and not visited[dx][dy]:
                    q.append((dx, dy))
                    maps[dx][dy] += maps[x][y]

        return maps

    maps = bfs(0, 0)

    if maps[n - 1][m - 1] > 1:
        answer = maps[n - 1][m - 1]
    else:
        answer = -1

    return answer