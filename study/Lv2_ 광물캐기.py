from collections import Counter


def solution(picks, minerals):
    answer = 0

    if len(minerals) > 5 * sum(picks):
        minerals = minerals[:5 * sum(picks)]  # 5개로 끊어지지 않을 때 남는거는 버려짐

    result = []
    for i in range(0, len(minerals), 5):
        temp = minerals[i:i + 5]
        cnt = Counter(temp)
        result.append((cnt['diamond'], cnt['iron'], cnt['stone']))

    result.sort(reverse=True)  # 다이아가 많은 순으로 정렬

    for a, b, c in result:
        if picks[0] > 0:  # 다이아 곡괭이가 있으면
            answer += a * 1 + b * 1 + c * 1
            picks[0] -= 1
        elif picks[1] > 0:
            answer += a * 5 + b * 1 + c * 1
            picks[1] -= 1
        else:
            answer += a * 25 + b * 5 + c * 1
            picks[2] -= 1

    return answer


print(solution([1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]))
print(solution([0, 1, 1],
               ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron",
                "diamond"]))
