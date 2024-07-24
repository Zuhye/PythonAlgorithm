def solution(msg):
    alphabet = [0, "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                "U", "V", "W", "X", "Y", "Z"]
    answer = []
    i = 0

    while i < len(msg):
        text = msg[i]
        j = i + 1

        while j < len(msg) and text + msg[j] in alphabet:
            text = text + msg[j]
            j += 1

        if j < len(msg):
            alphabet.append(text + msg[j])

        idx = alphabet.index(text)
        answer.append(idx)

        i = j

    return answer


print(solution("KAKAO"))
# 	[11, 1, 27, 15]

print(solution("TOBEORNOTTOBEORTOBEORNOT"))
#  [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
