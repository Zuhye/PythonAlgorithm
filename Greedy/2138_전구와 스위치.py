import sys

input = sys.stdin.readline

N = int(input())
lights = list(map(int, input().rstrip()))
goal = list(map(int, input().rstrip()))
answer = 0

# 0번째 전구를 껐을 때와, 켰을 때 두 기준을 생각하면서 풀어야한다.
# 그 외에는 i번째 전구가 i-1번째 전구에 마지막 영향을 미치므로 i-1번째만 신경쓰면 된다.
# ---->  이런 생각을 어떻게 하지..?

def check(target, goal):
    temp = target[:]
    cnt = 0
    for i in range(1, N):
        if temp[i - 1] == goal[i - 1]:
            continue
        # 전구가 다를 경우에는 눌러야 한다
        cnt += 1
        for j in range(i - 1, i + 2):
            if j < N:
                temp[j] = 1 - temp[j]
    if temp == goal:
        return cnt
    else:
        return 1e9


# 0 번째 전구 적용 x
result = check(lights, goal)

# 0 번째 전구 적용 o

lights[0] = 1 - lights[0]
lights[1] = 1 - lights[1]

result2 = check(lights, goal) + 1

answer = min(result, result2)

if answer  != 1e9:
    print(answer)
else:
    print(-1)