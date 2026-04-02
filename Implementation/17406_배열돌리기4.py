import sys
from itertools import permutations
from copy import deepcopy

input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
rotate = [list(map(int, input().split())) for _ in range(K)]
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

result = int(1e9)

for i in permutations(rotate, K):
    temp = deepcopy(board) # 기존 board 복사
    for r, c, s in i:
        r -= 1
        c -= 1

        for j in range(s, 0, -1):
            tmp = temp[r-j][c+j]

            #위
            temp[r-j][c-j+1:c+j+1] = temp[r-j][c-j:c+j]

            #왼
            for row in range(r-j, r+j):
                temp[row][c-j] = temp[row+1][c-j]

            #아래
            temp[r+j][c-j:c+j] = temp[r+j][c-j+1:c+j+1]

            #오
            for row in range(r+j, r-j, -1):
                temp[row][c+j] = temp[row-1][c+j]

            temp[r-j+1][c+j] = tmp

    for i in temp:
        result = min(result, sum(i))

print(result)