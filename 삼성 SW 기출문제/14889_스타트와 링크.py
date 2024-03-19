import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
members = [i for i in range(N)]
teams = []
result = 10e9

for team in list(combinations(members, N // 2)):
    teams.append(team)

length = len(teams) // 2  # 3
for i in range(length):
    result1 = 0
    result2 = 0
    temp = teams[i]
    for j in range(N // 2):
        person = temp[j]  # 한 사람당
        for k in temp:  # 한 팀 구성 (0, 1)
            result1 += board[person][k]
    # 링크 팀
    tmp = teams[len(teams) - 1 - i]
    for j in range(N // 2):
        person = tmp[j]
        for k in tmp:
            result2 += board[person][k]

    if result > abs(result1 - result2):
        result = abs(result1 - result2)


print(result)
