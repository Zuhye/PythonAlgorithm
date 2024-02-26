def solution(n):
    answer = 0

    if n == 2:
        answer = 1

    if n % 2 == 0 and n > 2:
        # answer += 3 # 1, 2인 경우
        for i in range(2, n - 1):
            answer += 2 * (i ** 2)
        answer += (n - 1) ** 2 + 3

    if n % 2 != 0:
        for i in range(1, n-1):
            if i % 2 != 0:
                answer += 2*(i**2)
            else:
                answer += i**2 + 2*(i**2)
        answer += (n-1) ** 2
    return answer


print(solution(6))
# 20출력
