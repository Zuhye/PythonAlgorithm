def solution(gems):
    answer = []
    result = []
    ans = 10e9
    types = set(gems)

    for i in range(0, len(gems) - len(types) + 1):
        temp = []
        idx = []
        for j in range(i, len(gems)):
            if gems[j] not in temp:
                temp.append(gems[j])
                idx.append(j)

        if len(idx) == len(types):
            answer.append([idx[0] + 1, idx[-1] + 1])

    result = max(answer, key=lambda x: (-(x[1] - x[0]), -x[0]))
    print(answer, result)

    return result


##### 시간 초과 발생 ####

def solution2(gems):
    gem = len(set(gems))
    dic = {gems[0]: 1}
    answer = [0, len(gems) - 1]  # 답
    start, end = 0, 0

    while end < len(gems):
        if len(dic) == gem:
            if (end - start) < (answer[1] - answer[0]):
                answer = [start, end]

            dic[gems[start]] -= 1
            if dic[gems[start]] == 0:
                del dic[gems[start]]
            start += 1

        else:
            end += 1
            if end < len(gems):
                if gems[end] in dic:
                    dic[gems[end]] += 1
                else:
                    dic[gems[end]] = 1

    return [answer[0] + 1, answer[1] + 1]


print(solution2(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
# [3, 7] 출력

print(solution2(["AA", "AB", "AC", "AA", "AC"]))
# [1, 3] 출력

print(solution2(["XYZ", "XYZ", "XYZ"]))
# [1, 1] 출력
