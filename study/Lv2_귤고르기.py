from collections import Counter


def solution(k, tangerine):
    answer = 0

    result = Counter(tangerine)
    results = sorted(result.items(), key=lambda x: x[1], reverse=True)
    # (값, 개수)

    answer = 0

    for elem in results:
        k -= elem[1]
        answer += 1

        if k <= 0:
            break
    return answer


print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))  # 3 출력
print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))  # 2 출력
