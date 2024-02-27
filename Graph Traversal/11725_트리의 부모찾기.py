import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
visited = [False] * (N + 1)
answer = [0] * (N + 1)
board = [[] for _ in range(N + 1)]

for i in range(N - 1):
    s, e = map(int, input().split())
    board[s].append(e)
    board[e].append(s)


def bfs(board, e, visited):
    q = deque([e])
    visited[e] = True

    while q:
        x = q.popleft()
        for i in board[x]:
            if not visited[i]:
                answer[i] = x
                q.append(i)
                visited[i] = True


# def dfs(board, v, visited):
#     visited[v] = True
#
#     for i in board[v]:
#         if not visited[i]:
#             answer[i] = v
#             dfs(board, i, visited)

bfs(board, 1, visited)
# dfs(board, 1, visited)

for i in range(2, N + 1):
    print(answer[i])
