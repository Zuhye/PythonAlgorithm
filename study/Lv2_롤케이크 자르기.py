def solution(topping):
    answer = 0

    for i in range(len(topping)):
        lst1 = set(topping[:i])
        lst2 = set(topping[i:])
        if len(lst1) == len(lst2):
            answer += 1
    return answer

    # ------------------- 시간초과 - ------------------------------------


from collections import Counter


def solution2(topping):
    answer = 0
    cnts = Counter(topping)
    give = set()

    for i in topping:
        cnts[i] -= 1
        give.add(i)

        if cnts[i] == 0:
            cnts.pop(i)
        if len(cnts) == len(give):
            answer += 1
    return answer