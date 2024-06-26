import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]
dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
visited = set(board[0][0])  # 알파벳 방문 여부
answer = 0


def dfs(x, y, cnt):
    global answer

    answer = max(answer, cnt)

    for d in range(4):
        nx = x + dir[d][0]
        ny = y + dir[d][1]
        if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in visited:
            visited.add(board[nx][ny])
            dfs(nx, ny, cnt + 1)
            visited.remove(board[nx][ny])


dfs(0, 0, 1)
print(answer)
