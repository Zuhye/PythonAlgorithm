def find_max_candidates(a):
    # 서버 1과 서버 2에 대해 각각의 후보군을 시간 기준으로 정렬
    a.sort(key=lambda x: x[0])  # 서버 1 기준 정렬
    server1_candidates = [x[0] for x in a]
    a.sort(key=lambda x: x[1])  # 서버 2 기준 정렬
    server2_candidates = [x[1] for x in a]

    # 주어진 조건을 만족하는 최대 길이의 후보군을 찾는 함수
    def max_length(arr):
        max_len = 0
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if arr[j] > arr[i] * 2 or arr[j] - arr[i] >= 1000:
                    break
                max_len = max(max_len, j - i + 1)
        return max_len

    # 각 서버별로 조건을 만족하는 최대 후보군 길이를 찾음
    max_len1 = max_length(server1_candidates)
    max_len2 = max_length(server2_candidates)

    # 더 많은 후보를 포함할 수 있는 서버와 그 때의 후보의 수 반환
    if max_len1 > max_len2:
        return 1, max_len1
    else:
        return 2, max_len2


# 주어진 리스트
a = [[2423, 10], [3423, 30], [1, 40], [450, 50], [1200, 60], [2781, 100]]
print(find_max_candidates(a))
