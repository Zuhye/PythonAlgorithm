from collections import deque


def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]

    def bfs(computers, start, visited):
        visited[start] = True
        q = deque([start])

        while q:
            x = q.popleft()

            for i in range(n):
                if computers[x][i] == 1 and not visited[i]:
                    visited[i] = True
                    q.append(i)

    for i in range(n):
        if not visited[i]:
            bfs(computers, i, visited)
            answer += 1

    return answer


print(solution([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))  # 2 출력
print(solution([[1, 1, 0], [1, 1, 1], [0, 1, 1]]))  # 1 출력
