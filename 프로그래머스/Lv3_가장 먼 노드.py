from collections import deque


def solution(n, edge):
    answer = 0
    board = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)

    for i in edge:
        board[i[0]].append(i[1])
        board[i[1]].append(i[0])

    q = deque()
    q.append(1)  # 출발 노드 = 1
    visited[1] = 1

    while q:

        node = q.popleft()

        for i in board[node]:
            if not visited[i]:
                visited[i] = visited[node] + 1
                q.append(i)

    for i in visited:
        if i == max(visited):
            answer += 1

    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
# 3출력
