import sys

input = sys.stdin.readline


def solution1():
    N = int(input())
    scores = [list(map(int, input().split())) for _ in range(3)]
    rank = [[0] * N for _ in range(4)]

    for i in range(3):
        for j in range(N):
            cur = scores[i][j]
            cnt = 0

            for k in range(N):
                if k == j:
                    continue
                if cur < scores[i][k]:
                    cnt += 1
            rank[i][j] = cnt + 1

    total = [0] * N
    for i in range(N):
        for j in range(3):
            total[i] += scores[j][i]

    for i in range(N):
        cur = total[i]
        cnt = 0
        for j in range(N):
            if i == j:
                continue
            if cur < total[j]:
                cnt += 1
        rank[3][i] = cnt + 1

    for i in rank:
        print(*i)


# ----------------------- 복잡도 낮춘 방법 ---------------

def solution2():
    N = int(input())
    scores = [list(map(int, input().split())) for _ in range(3)]
    ranks = [[0] * N for _ in range(4)]

    for i in range(3):
        sorted_scores = sorted(((score, idx) for idx, score in enumerate(scores[i])), reverse=True)
        rank = 1

        for j in range(N):
            if j > 0 and sorted_scores[j][0] < sorted_scores[j - 1][0]:
                rank = j + 1

            ranks[i][sorted_scores[j][1]] = rank

    total = [sum(scores[j][i] for j in range(3)) for i in range(N)]

    sorted_total_scores = sorted(((score, idx) for idx, score in enumerate(total)), reverse=True)
    rank = 1

    for j in range(N):
        if j > 0 and sorted_total_scores[j][0] < sorted_total_scores[j - 1][0]:
            rank = j + 1
        ranks[3][sorted_total_scores[j][1]] = rank

    return ranks


result = solution2()
for i in result:
    print(*i)
