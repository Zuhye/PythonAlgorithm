import sys
from itertools import combinations

input = sys.stdin.readline


def solution1():
    N = int(input())
    honey = list(map(int, input().split()))
    h_idx = N - 1  # 꿀통 인덱스 (제일 마지막)

    answer = 0

    while h_idx >= 0:
        for a, b, in combinations(range(0, N), 2):
            if h_idx != a and h_idx != b:
                total = 0
                if h_idx > b and h_idx > a:
                    first = honey[a + 1: b] + honey[b + 1:h_idx + 1]
                    second = honey[b + 1: h_idx + 1]
                elif a <= h_idx <= b:
                    first = honey[a + 1:h_idx + 1]
                    second = honey[h_idx:b]
                elif h_idx < a and h_idx < b:
                    first = honey[h_idx:a]
                    second = honey[a + 1:b] + honey[h_idx:a]

                total = sum(first) + sum(second)
                answer = max(answer, total)
        h_idx -= 1

    print(answer)


# solution1()


def solution2():
    N = int(input())
    honey = list(map(int, input().split()))

    # 누적합 배열 생성
    prefix_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_sum[i] = prefix_sum[i - 1] + honey[i - 1]
    answer = 0

    # 벌통이 가장 왼쪽에 있을 때
    for i in range(1, N - 1):
        total = prefix_sum[N - 1] + (prefix_sum[i] - honey[i])
        answer = max(answer, total)

    # 벌통이 가장 오른쪽에 있을 때
    for i in range(1, N - 1):
        total = (prefix_sum[N] - honey[0]) + (prefix_sum[N] - prefix_sum[i + 1] - honey[i])
        answer = max(answer, total)

    # 벌통이 제일 가운데 있을 때 꿀벌은 양 옆이 고정이고 벌통 위치를 탐색
    for i in range(1, N - 1):
        total = prefix_sum[N - 1] - honey[0] + honey[i]
        answer = max(answer, total)

    print(answer)


solution2()
