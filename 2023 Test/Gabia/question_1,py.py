def solution(a):
    answer = []
    for i in a:
        result = 0
        if i not in "b":
            result = True
            answer.append(result)
            continue

            temp = "bab"
            index = i.index("bab")
            if i[index - 1] == "a":
                temp = i[index - 1:]
            elif i[index + 3] == "a":
                temp = i[index:index + 4]

            print(temp)


    return answer


print(solution(["abab", "bbaa", "bababa", "bbbabababbbaa"]))
# [true, false, false, true] 반환

