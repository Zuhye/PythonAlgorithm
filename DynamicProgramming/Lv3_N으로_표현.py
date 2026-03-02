def solution(N, number):
    answer = -1

    if N == number:
        return 1

    arr = [set() for _ in range(8)]

    for i in range(len(arr)):
        arr[i].add(int(str(N) * (i + 1)))

    for i in range(1, 8):
        for j in range(i):
            for op1 in arr[j]:
                for op2 in arr[i - j - 1]:
                    arr[i].add(op1 + op2)
                    arr[i].add(op1 - op2)
                    arr[i].add(op1 * op2)
                    if op2 != 0:
                        arr[i].add(op1 // op2)

        if number in arr[i]:
            answer = i + 1
            break

    return answer


print(solution(5, 12))  # 답: 4
print(solution(2, 11))  # 답: 3
