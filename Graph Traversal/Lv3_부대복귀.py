from collections import deque, defaultdict


def solution(n, roads, sources, destination):
    graph = defaultdict(list)
    visited = [-1] * (n + 1)
    answer = []

    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    q = deque()
    q.append(destination)

    visited[destination] = 0

    while q:
        now = q.popleft()

        for n in graph[now]:
            if visited[n] == -1:  # 방문을 하지 않았다면
                q.append(n)
                visited[n] = visited[now] + 1

    for value in sources:
        answer.append(visited[value])

    return answer


print(solution(3, [[1, 2], [2, 3]], [2, 3], 1)) # 답: [1, 2]
print(solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5)) # 답: [2, -1, 0
