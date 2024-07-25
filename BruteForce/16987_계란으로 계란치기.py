import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)]
answer = 0


def dfs(n, cnt):
    global answer

    if answer >= (cnt + (N - n) * 2):  # 끝까지 진행해도 정답 갱신 불가능 한 경우
        return

    if n == N:  # 종료 조건: 모든 계란을 손에 들고 부딪침
        answer = max(answer, cnt)
        return
    if eggs[n][0] <= 0:  # 내 계란이 깨진 경우
        dfs(n + 1, cnt)
    else:  # 현재 계란 안깨진 경우
        flag = False  # 한번도 안부딪혔다면 .. 그래도 다음 계란으로 가야함
        for j in range(N):  # 하나씩 깨보기 시작
            if n == j or eggs[j][0] <= 0:
                continue
            flag = True
            eggs[n][0] -= eggs[j][1]
            eggs[j][0] -= eggs[n][1]

            dfs(n + 1, cnt + int(eggs[n][0] <= 0) + int(eggs[j][0] <= 0))

            eggs[n][0] += eggs[j][1]  # 원상복구
            eggs[j][0] += eggs[n][1]

        if not flag:
            dfs(n + 1, cnt)


dfs(0, 0)
print(answer)
