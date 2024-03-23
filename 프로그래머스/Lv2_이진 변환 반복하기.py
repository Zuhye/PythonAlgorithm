def solution(s):
    answer = [0, 0]
    cnt = 0
    result = 0

    while s != "1":
        cnt += s.count("0")
        s = s.replace("0", "")
        length = len(s)
        s = format(length, 'b')
        result += 1
    answer[0] = result
    answer[1] = cnt
    return answer

print(solution("110010101001"))