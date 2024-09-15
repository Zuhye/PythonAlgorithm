from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []

    # 각각의 order는 정렬
    orders = [''.join(sorted(order)) for order in orders]

    for i in course:
        com = []

        for j in orders:
            com += combinations(j, i)

        cnt = Counter(com)

        if cnt:
            value = max(cnt.values())
            if value >= 2:
                for a, v in cnt.items():
                    if v == value:
                        answer.append(''.join(a))

    return sorted(answer)


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
# ["AC", "ACDE", "BCFG", "CDE"] 출력
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
# ["ACD", "AD", "ADE", "CD", "XYZ"] 출력
