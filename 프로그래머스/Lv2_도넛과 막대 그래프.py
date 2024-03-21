def solution(edges):
    answer = [0, 0, 0, 0]
    # 생성한 정점의 번호, 도넛 수, 막대 수, 8자 모양 수
    # 각 개수는 생성된 정점 전의 수
    cnt = {}

    for a, b in edges:

        if a not in cnt:  # a: 나간거(out)
            cnt[a] = [0, 0]
        if b not in cnt:  # b: 받은거(in)
            cnt[b] = [0, 0]

        cnt[a][0] += 1
        cnt[b][1] += 1

    for key, values in cnt.items():
        if values[0] >= 2 and values[1] == 0:  # 생성한 정점 번호
            answer[0] = key
        if values[0] == 0 and values[1] > 0:  # 막대 수 (나가는거 0, 받는거 1 이상)
            answer[2] += 1
        if values[0] >= 2 and values[1] >= 2:  # 8자 수
            answer[3] += 1

    answer[1] = cnt[answer[0]][0] - (answer[2] + answer[3])

    return answer


print(solution([[2, 3], [4, 3], [1, 1], [2, 1]]))
