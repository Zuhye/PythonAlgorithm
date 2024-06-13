def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]

    # 첫번째 스티커를 떼는 경우: 마지막 idx 확인 x
    dp = [0 for _ in range(len(sticker))]
    dp[0] = sticker[0]
    dp[1] = dp[0]

    for i in range(2, len(sticker) - 1):
        dp[i] = max(sticker[i] + dp[i - 2], dp[i - 1])

    # 첫번째 스티커를 안떼는 경우: 마지막 idx까지 확인
    dp2 = [0 for _ in range(len(sticker))]
    dp2[0] = 0
    dp2[1] = sticker[1]

    for i in range(2, len(sticker)):
        dp2[i] = max(sticker[i] + dp2[i - 2], dp2[i - 1])

    return max(max(dp), max(dp2))


print(solution([14, 6, 5, 11, 3, 9, 2, 10]))  # 36 출력
print(solution([1, 3, 2, 5, 4]))  # 8 출력
