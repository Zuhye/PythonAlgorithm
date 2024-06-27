import sys
from itertools import permutations

input = sys.stdin.readline

N, M = map(int, input().split())


def solution1():
    result = list(permutations([i for i in range(1, N + 1)], M))
    for i in result:
        print(*i)


ans = []
v = [0] * (N + 1)


def dfs(n, lst):
    # 종료 조건은 n과 관련된 것으로 두고, 제일 위에 작성하기
    if n == M:
        ans.append(lst)

    for i in range(1, N + 1):
        if v[i] == 0:
            v[i] = 1
            dfs(n + 1, lst + [i])
            v[i] = 0


dfs(0, [])
for i in ans:
    print(*i)
