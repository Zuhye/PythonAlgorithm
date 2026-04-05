import sys
from itertools import combinations, permutations

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
P, X = map(int, input().split())

answer = 0

# 1. 숫자 순열
for perm in permutations(nums):
    print(perm)
    # 2. * 위치 선택 (조합)
    for comb in combinations(range(N - 1), X):
        op = ['+'] * (N - 1)
        for idx in comb:
            op[idx] = '*'

        # 3. 계산 (괄호 효과 반영)
        groups = []
        cur_sum = perm[0]

        for i in range(N - 1):
            if op[i] == '+':
                cur_sum += perm[i + 1]
            else:  # '*'
                groups.append(cur_sum)
                cur_sum = perm[i + 1]

        groups.append(cur_sum)  # 마지막 묶음

        # 4. 곱하기
        result = 1
        for g in groups:
            result *= g

        answer = max(answer, result)

print(answer)