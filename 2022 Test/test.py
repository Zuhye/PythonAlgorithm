# 11724 - 연결요소의 개수 2178 - 미로탐색
import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
adj = [[0]*N for _ in range(N)]
visited = [False]* N
count = 0

for _ in range(M):
    u, v = map(lambda x:x-1, map(int, input().split()))
    adj[u][v] = adj[v][u] = 1
#
# for row in range(N):
#     print(adj[row])

def dfs(now):
    for nxt in range(N):
        if adj[now][nxt] and not visited[nxt]:
            visited[nxt] = True
            dfs(nxt)

for i in range(N):
    if not visited[i]:
        count+=1
        visited[i] = True
        dfs(i)

print(count)