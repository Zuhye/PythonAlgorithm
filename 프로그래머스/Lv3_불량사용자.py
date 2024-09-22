from itertools import permutations


def check(users, banned_id):
    for i in range(len(banned_id)):
        if len(users[i]) != len(banned_id[i]):  # 길이가 같지 않으면 False
            return False

        for j in range(len(users[i])):  # 각 단어의 길이만큼 반복문
            if banned_id[i][j] == "*":
                continue
            if banned_id[i][j] != users[i][j]:
                return False
    return True


def solution(user_id, banned_id):
    answer = set()
    user_permutation = list(permutations(user_id, len(banned_id)))

    for users in user_permutation:
        if not check(users, banned_id):
            continue
        else:  # 해당이 되면 저장
            users = frozenset(users)
            if users not in answer:
                answer.add(users)
    return len(answer)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
# 2출력

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
# 2출력

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
# 3출력
