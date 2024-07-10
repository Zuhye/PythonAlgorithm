import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
ladder = dict(map(int, input().split()) for _ in range(N))
snake = dict(map(int, input().split()) for _ in range(M))
visited = [0] * 101


def bfs(start, end):
    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        c = q.popleft()

        for i in (c + 1, c + 2, c + 3, c + 4, c + 5, c + 6):
            n = i

            if n > 100:
                continue

            if n == end:
                return visited[c]

            if n in ladder:
                n = ladder[n]
            elif n in snake:
                n = snake[n]

            if not visited[n]:
                q.append(n)
                visited[n] = visited[c] + 1

                if n == end:
                    return visited[n]


print(bfs(1, 100))
