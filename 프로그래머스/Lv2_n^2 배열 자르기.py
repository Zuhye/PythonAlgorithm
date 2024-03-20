def solution(n, left, right):
    answer = []

    for i in range(left, right + 1):
        x = i // n
        y = i % n

        if x > y:
            answer.append(x + 1)
        else:
            answer.append(y + 1)

    return answer


print(solution(3, 2, 5))
