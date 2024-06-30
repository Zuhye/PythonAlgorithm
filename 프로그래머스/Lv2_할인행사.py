from collections import Counter


def solution(want, number, discount):
    cnt = 0

    if sum(number) != 10:
        return cnt

    # 원하는 물건이 없는 경우
    for i in want:
        if i not in discount:
            return cnt

    for i in range(0, len(discount) - 9):
        temp = discount[i:i + 10]
        result = Counter(temp)
        flag = True

        for i in range(len(want)):
            if result[want[i]] != number[i]:
                flag = False
                break
        if flag:
            print(temp)
            cnt += 1
    return cnt


print(solution(["apple"], [10],
         ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))
