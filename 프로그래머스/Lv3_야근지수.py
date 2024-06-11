from itertools import combinations_with_replacement
import copy
import sys
import heapq


def solution(n, works):
    answer = sys.maxsize
    idx = [i for i in range(len(works))]

    for cwr in combinations_with_replacement(idx, n):
        temp = copy.deepcopy(works)
        value = 0

        for i in cwr:
            temp[i] -= 1
            if temp[i] < 0:
                temp[i] = 0

        for j in temp:
            value += j ** 2

        if value < answer:
            answer = value

    return answer


# -----------시간초과-----------------------#


def solution2(n, works):
    answer = 0

    if sum(works) <= n:
        return 0

    works = [-work for work in works]
    heapq.heapify(works)
    print(works)

    for i in range(n):
        if not works:
            break

        value = heapq.heappop(works)

        if value == 0:
            break
        value += 1
        heapq.heappush(works, value)

    answer = sum(work ** 2 for work in works)
    return answer


print(solution2(4, [4, 3, 3]))
# 12출력
