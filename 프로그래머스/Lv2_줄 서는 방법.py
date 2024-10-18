import math


def solution(n, k):
    answer = []
    numbers = [i for i in range(1, n + 1)]  # 사용할 숫자들
    k -= 1

    while n > 0:
        n -= 1
        # 현재 자리에 올 숫자를 결정하기 위한 인덱스 계산
        fact = math.factorial(n)
        index = k // fact
        answer.append(numbers.pop(index))

        k %= fact  # k를 갱신 -> 새로 정한 그룹에서 몇번째 인지 다시 계산

    return answer


print(solution(3, 5))
# [3, 1, 2] 출력
