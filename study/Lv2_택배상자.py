def solution(order):
    answer = 0
    stack = []
    cnt = 0

    for i in order:
        while cnt < i:
            cnt += 1
            stack.append(cnt)

        if stack and stack[-1] == i:
            answer += 1
            stack.pop()
        else:
            break

    return answer


print(solution([4, 3, 1, 2, 5]))
# 2 출력
