def solution(n, stations, w):
    answer = 0
    spread = 2 * w + 1

    prev_end = 0
    for i in stations:
        start = max(1, i - w)  # 전파 시작점
        if start > prev_end + 1:
            gap = start - (prev_end + 1)
            answer += (gap + spread - 1) // spread  # 필요한 기지국 수
        prev_end = min(n, i + w)  # 기지국 전파 끝점

    # 마지막 기지국 이후 처리
    if prev_end < n:
        gap = n - prev_end
        answer += (gap + spread - 1) // spread

    return answer


print(solution(11, [4, 11], 1))  # 3출력
print(solution(16, [9], 2))  # 3 출력
