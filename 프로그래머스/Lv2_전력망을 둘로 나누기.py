from collections import deque


def cnt(start, end, visited, trees):
    q = deque([start])
    visited[start] = True
    cnt = 1

    while q:
        cur = q.popleft()
        for i in trees[cur]:
            if not visited[i] and i != end:
                q.append(i)
                visited[i] = True
                cnt += 1
    return cnt


def solution(n, wires):
    answer = 10e9
    trees = [[] for _ in range(n + 1)]

    for a, b in wires:
        trees[a].append(b)
        trees[b].append(a)

    for a, b in wires:
        visited = [False] * (n + 1)
        result1 = cnt(a, b, visited, trees)
        result2 = cnt(b, a, visited, trees)

        result = abs(result1 - result2)

        if result < answer:
            answer = result

    return answer


print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))