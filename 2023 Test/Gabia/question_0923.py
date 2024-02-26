from math import comb
from math import factorial


def solution(n, nationality):
    answer = -1
    same = []

    nationality.sort(key=lambda x: [x[0], x[1]])

    for pair in nationality:
        student1, student2 = pair
        flag = False

        for i in same:
            if student1 in i or student2 in i:
                i.add(student1)
                i.add(student2)
                flag = True
                break

        if not flag:
            new = {student1, student2}
            same.append(new)

    same = [list(j) for j in same]
    print(same)

    dupli = 0

    for i in same:
        dupli += comb(len(i), 2)

    answer = comb(n, 2) - dupli

    return answer


print(solution(5, [[1, 2], [2, 3]]))
