import sys
from itertools import combinations

input = sys.stdin.readline

def solution1():
    N, M = map(int, input().split())
    relation = [[] for _ in range(N + 1)]
    result = 1e9

    for i in range(M):
        a, b = map(int, input().split())
        relation[a].append(b)
        relation[b].append(a)

    for comb in combinations(range(1, N + 1), 3):
        a, b, c = comb

        if b in relation[a] and c in relation[a] and a in relation[b] and c in relation[b] and a in relation[c] and b in relation[c]:
            cnt = len(relation[a]) + len(relation[b]) + len(relation[c]) - 6
            result = min(result, cnt)
    if result == 1e9:
        result = -1
    print(result)


def solution2():
    N, M = map(int, input().split())
    relation = {}
    result = 1e9

    for _ in range(M):
        a, b = map(int, input().split())

        if relation.get(a):
            relation[a].append(b)
        else:
            relation[a] = [b]

        if relation.get(b):
            relation[b].append(a)
        else:
            relation[b] = [a]

    for A in range(1, N + 1):
        if not relation.get(A):
            continue

        for B in relation[A]:
            for C in relation[A]:
                if B == C:
                    continue
                if C in relation[B]:
                    result = min(result, len(relation[A]) + len(relation[B]) + len(relation[C]) - 6 )
    if result == 1e9:
        print(-1)
    else:
        print(result)
solution2()