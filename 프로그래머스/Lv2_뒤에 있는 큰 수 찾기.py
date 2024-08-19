def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []

    for i in range(len(numbers)):
        x = numbers[i]

        while stack and numbers[stack[-1]] < x:
            idx = stack.pop()
            answer[idx] = x
        stack.append(i)

    return answer


print(solution([-1, 3, 3, 5, 6]))
