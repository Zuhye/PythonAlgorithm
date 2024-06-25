import sys

input = sys.stdin.readline

n = int(input())  # 전체 사람 수
a, b = map(int, input().split())  # 구해야 하는 두 사람 번호
m = int(input())
relations = [[] for _ in range(n + 1)]
flag = False

for i in range(m):
    x, y = map(int, input().split())
    relations[x].append(y)
    relations[y].append(x)

visited = [0] * (n + 1)


def dfs(start, count):
    global flag
    count += 1
    visited[start] = 1

    if start == b:
        flag = True
        print("dfs: ", count - 1)
    for i in relations[start]:
        if not visited[i]:
            dfs(i, count)


def bfs(start, end):
    global n
    q = []
    v = [0] * (n + 1)

    q.append(start)
    v[start] = 1

    while q:
        c = q.pop(0)

        if c == end:
            return v[end] - 1

        # c와 연결된 번호인 경우 미방문이면 방문!
        for n in relations[c]:
            if not v[n]:
                q.append(n)
                v[n] += v[c] + 1

    # 이곳의 코드를 실행했다면 ... 찾지 못함
    return -1


dfs(a, 0)
if not flag:
    print(-1)

ans = bfs(a, b)
print("bfs: ", ans)
