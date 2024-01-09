# 첫 줄에는 전체 사람의 수 N이 주어진다. 그리고 이어지는 N개의 줄에는 각 사람의 몸무게와 키를 나타내는 양의 정수 x와 y가 하나의 공백을 두고 각각 나타난다.
# 2 ≤ N ≤ 50
# 10 ≤ x, y ≤ 200

N = int(input())
info = []

for i in range(N):
    w, h = map(int, input().split())
    info.append((w, h))

for i in info:
    ranking = 1
    for j in info:
        if i[0] < j[0] and i[1] < j[1]:
            ranking += 1
    print(ranking, end=' ')