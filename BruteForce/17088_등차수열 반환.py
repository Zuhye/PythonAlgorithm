import sys

input = sys.stdin.readline

N = int(input())
B = list(map(int, input().split()))

answer = 1e9


def check(i, j):
    cnt = abs(i) + abs(j)  # 연산 횟수
    arr = [B[1] + j]  # 새로 저장할 배열
    diff = (B[1] + j) - (B[0] + i)  # 공차

    for k in range(2, N):  # 세번쨰 원소부터 확인

        if B[k] == arr[k - 2] + diff:
            arr.append(B[k])
        elif B[k] - 1 == arr[k - 2] + diff:
            arr.append(B[k] - 1)
            cnt += 1
        elif B[k] + 1 == arr[k - 2] + diff:
            arr.append(B[k] + 1)
            cnt += 1
        else:
            return False

    return cnt


if N <= 2:  # 입력 수가 2 이하면 무조건 등차수열
    print(0)
    exit()
else:
    for i in range(-1, 2):
        for j in range(-1, 2):
            result = check(i, j)
            if not result:
                continue
            else:
                answer = min(answer, result)

if answer == 1e9:
    print(-1)
else:
    print(answer)
