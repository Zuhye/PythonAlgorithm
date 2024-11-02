def solution(skill, skill_trees):
    valid_count = 0  # 가능한 스킬 트리 개수

    for skill_tree in skill_trees:
        temp = []
        for s in skill_tree:
            if s in skill:
                temp.append(s)
        # skill에서 등장한 순서대로만 필터링해서 순서를 맞추기 위해
        filtered_skill = ''.join(temp)
        print(filtered_skill)

        # 스킬 순서가 정확하게 일치하는 경우만 count 증가
        if filtered_skill == skill[:len(filtered_skill)]:
            valid_count += 1

    return valid_count


# 예제
skill = "ACD"
skill_trees = ["ACDE", "ABCD", "ADC", "BABCED"]
print(solution(skill, skill_trees))  # 예상 결과: 2
