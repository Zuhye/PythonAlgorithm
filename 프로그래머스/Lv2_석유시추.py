from collections import deque

dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def bfs(land, x, y, id):
    q = deque()
    q.append((x, y))
    cnt = 0  # 초기 크기는 0
    land[x][y] = id

    while q:
        x, y = q.popleft()
        cnt += 1

        for d in range(4):
            dx = x + dir[d][0]
            dy = y + dir[d][1]

            if 0 <= dx < len(land) and 0 <= dy < len(land[0]):
                if land[dx][dy] == 1:
                    land[dx][dy] = id  # 같은 인덱스 설정
                    q.append((dx, dy))

    return cnt


def solution(land):
    id = 2
    answer = 0
    oil = {}  # 각 석유 크기 저장

    for i in range(len(land)):
        for j in range(len(land[0])):
            if land[i][j] == 1:
                oil[id] = bfs(land, i, j, id)
                id += 1

    for i in range(len(land[0])):
        unique_ids = set()  # 현재 열을 지나는 유일한 크기
        for j in range(len(land)):
            if land[j][i] > 1:
                unique_ids.add(land[j][i])

        sum = 0
        for id in unique_ids:
            sum += oil[id]

        if sum > answer:
            answer = sum

    return answer


print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0],
          [1, 1, 1, 0, 0, 0, 1, 1]])
)