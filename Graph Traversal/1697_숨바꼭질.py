import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())  # N: 수빈이 위치 / M: 동생 위치
visited = [0] * 200001

# --- 최소 시간: bfs -----


def bfs(s, e):
    q = deque()
    q.append(s)
    visited[s] = 1

    while q:
        c = q.popleft()

        if c == e:
            return visited[e] - 1

        for i in (c - 1, c + 1, c * 2):
            if 0 <= i <= 200000 and not visited[i]:
                q.append(i)
                visited[i] = visited[c] + 1
    return -1


ans = bfs(N, K)
print(ans)
