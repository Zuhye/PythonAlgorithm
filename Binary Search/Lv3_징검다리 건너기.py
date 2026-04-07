def solution(stones, k):
    answer = 0
    left = 1
    right = max(stones)

    def cross(value):
        cnt = 0

        for i in stones:
            if i - value < 0:  # 못 건너는 경우
                cnt += 1
            else:
                cnt = 0

            if cnt >= k:
                return False
        return True

    while left <= right:
        mid = (left + right) // 2

        if cross(mid):  ## 건널 수 있다면....
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)) # result: 3