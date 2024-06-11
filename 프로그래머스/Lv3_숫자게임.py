from collections import deque


def solution(A, B):
    answer = -1

    A.sort(reverse=True)
    B.sort(reverse=True)

    q = deque(B)

    for i in range(len(A)):
        if A[i] < q[0]:
            q.popleft()
            answer += 1
        else:
            q.pop()  # 최소값 제거

    return answer + 1


print(solution([5, 1, 3, 7], [2, 2, 6, 8]))
# 3 출력
print(solution([2, 2, 2, 2], [1, 1, 1, 1]))
# 0 출력