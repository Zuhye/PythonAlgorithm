def solution(begin, target, words):
    answer = 0

    def check(begin, word):
        cnt = 0  # 틀린 알파벳 개수 -> 1인경우 return
        for s, e in zip(begin, word):
            if s != e:
                cnt += 1
        if cnt == 1:
            return True
        return False

    if target not in words:
        return 0

    for i in words:

        if check(begin, target):
            answer += 1
            return answer

        if check(begin, i):
            answer += 1
            begin = i

    return answer