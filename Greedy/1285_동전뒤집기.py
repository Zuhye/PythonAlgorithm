import sys
import copy

input = sys.stdin.readline

N = int(input())
board = [list(input().rstrip()) for _ in range(N)]
answer = N * N

for bit in range(1 << N): # 생성되는 비트
    temp = [row[:] for row in board] # 얕은 복사
    for i in range(N):  # bit의 행 확인
        if bit & (1 << i): # bit의 i번째 비트가 1일 때 참이 된다
            for j in range(N):
                if temp[i][j] == 'H':
                    temp[i][j] = "T"
                else:
                    temp[i][j] = "H"
    cnt = 0
    # 열에서 T 개수 확인
    for i in range(N):
        tmp = 0
        for j in range(N):
            if temp[j][i] == 'T':
                tmp += 1
        cnt += min(tmp, N - tmp)
    answer = min(cnt, answer)
print(answer)