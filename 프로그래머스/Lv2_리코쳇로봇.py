from collections import deque


def solution(board):
    n = len(board)
    m = len(board[0])
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    answer = -1
    q = deque()
    visited = [[0] * len(board[0]) for _ in range(len(board))]

    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                sx, sy = i, j
    q.append((sx, sy, 0))

    while q:
        x, y, cnt = q.popleft()

        if board[x][y] == "G":
            answer = cnt
            break

        for dx, dy in dir:
            scope = 1
            while 1:
                nx = x + dx * scope
                ny = y + dy * scope

                if nx < 0 or nx >= n or ny < 0 or ny >= m or board[nx][ny] == "D":
                    if visited[nx - dx][ny - dy] == 0:
                        visited[nx - dx][ny - dy] = 1
                        q.append((nx - dx, ny - dy, cnt + 1))

                    break
                scope += 1  # 벽이나 장애물이 부딪치지 않으면 미끄러짐 + 1

    return answer


print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
# 7출력
print(solution([".D.R", "....", ".G..", "...D"]))
# -1 출력
