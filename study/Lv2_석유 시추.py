from collections import deque


def solution(land):
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    answer = 0
    N = len(land)
    M = len(land[0])

    def bfs(i, j, id):
        q = deque()
        q.append((i, j))
        cnt = 0
        land[i][j] = id

        while q:
            x, y = q.popleft()
            cnt += 1

            for d in range(4):
                nx = x + dir[d][0]
                ny = y + dir[d][1]

                if 0 <= nx < N and 0 <= ny < M and land[nx][ny] == 1:
                    q.append((nx, ny))
                    land[nx][ny] = id

        return cnt

    oil = {}
    id = 2
    for i in range(N):
        for j in range(M):
            if land[i][j] == 1:
                cnt = bfs(i, j, id)
                oil[id] = cnt
                id += 1

    for i in range(M):  # 열 마다 id 탐색
        ids = set()  # 중복되지 않는 id 저장
        for j in range(N):
            if land[j][i] >= 2:
                ids.add(land[j][i])

        total = 0
        for k in ids:
            total += oil[k]

        if total > answer:
            answer = total

    return answer


print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0, 1, 1]]))
