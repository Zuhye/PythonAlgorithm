def solution(land):
    for i in range(1, len(land)):
        # 이전 행에서 연속으로 밟을 수 없는 같은 열을 제외한 나머지 중 최대값을 더해줌
        land[i][0] += max(land[i - 1][1], land[i - 1][2], land[i - 1][3])
        land[i][1] += max(land[i - 1][0], land[i - 1][2], land[i - 1][3])
        land[i][2] += max(land[i - 1][0], land[i - 1][1], land[i - 1][3])
        land[i][3] += max(land[i - 1][0], land[i - 1][1], land[i - 1][2])

    # 마지막 행에서 얻을 수 있는 최대값을 리턴
    return max(land[-1])


print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))
#  16 출력
