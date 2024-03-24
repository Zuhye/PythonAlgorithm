from itertools import permutations


def solution(k, dungeons):
    answer = 0
    kk = k
    dungeons.sort(key=lambda x: (-x[0], -x[1]))
    result = list(permutations(dungeons, len(dungeons)))
    for step in result:
        cnt = 0
        for i in step:
            if k >= i[0]:
                k -= i[1]
                cnt += 1
        k = kk
        answer = max(cnt, answer)

    return answer


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
