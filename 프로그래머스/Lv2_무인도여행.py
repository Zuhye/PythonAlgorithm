from collections import deque


def solution(maps):
    answer = []
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    maps = [list(row) for row in maps]  # 문자열을 리스트로 변환
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]

    def bfs(i, j):
        q = deque()
        q.append((i, j))
        visited[i][j] = 1
        total = int(maps[i][j])

        while q:
            x, y = q.popleft()

            for d in range(4):
                nx = x + dir[d][0]
                ny = y + dir[d][1]

                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                    if visited[nx][ny] == 0 and maps[nx][ny] != "X":
                        total += int(maps[nx][ny])
                        q.append((nx, ny))
                        visited[nx][ny] = 1
        return total

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != "X" and visited[i][j] == 0:
                value = bfs(i, j)
                answer.append(value)

    if answer:
        return sorted(answer)
    else:
        return [-1]


print(solution(["X591X", "X1X5X", "X231X", "1XXX1"]))
# [1, 1, 27] 출력
