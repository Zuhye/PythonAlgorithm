import sys
from collections import deque

input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())
visited = [0] * (F+1)


def bfs(start, end):
    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        c = q.popleft()

        if c == end:
            return visited[end] -1

        for i in (c + U, c - D):
            if 0 < i <= F and not visited[i]:
                q.append(i)
                visited[i] = visited[c] + 1
    return "use the stairs"


ans = bfs(S, G)
print(ans)