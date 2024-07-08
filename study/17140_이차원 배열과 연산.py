import sys
from collections import Counter

input = sys.stdin.readline

r, c, k = map(int, input().split())  # A[r][c]가 k가 되는 최소 시간을 구함
A = [list(map(int, input().split())) for _ in range(3)]
width = len(A[0])
height = len(A)
time = 0


def r_calculation():
    global A
    temp = []

    for i in A:
        element = set(i)
        tmp = []
        tmp2 = []

        for j in element:
            if j == 0:
                continue
            cnt = i.count(j)
            tmp.append((j, cnt))
        tmp.sort(key=lambda x: (x[1], x[0]))

        for k in tmp:
            tmp2.append(k[0])
            tmp2.append(k[1])
        tmp2 = tmp2[:100]

        temp.append(tmp2)

        max_len = max(map(len, temp))

        for i in range(len(temp)):
            while len(temp[i]) != max_len:
                temp[i].append(0)
        A = temp


while True:

    if 0 <= r - 1 < len(A) and 0 <= c - 1 < len(A[0]) and A[r - 1][c - 1] == k:
        print(time)
        break

    if time > 100:
        print(-1)
        break

    if len(A) >= len(A[0]):
        r_calculation()
    else:
        A = list(map(list, zip(*A)))
        r_calculation()
        A = list(map(list, zip(*A)))

    time += 1


