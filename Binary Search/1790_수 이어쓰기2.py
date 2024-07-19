import sys

input = sys.stdin.readline

N, K = map(int, input().split())

ans = 0  # 현재 수
num = 1  # 자릿 수
nine = 9  # 현재 자릿수의 최대 숫자

while K > num * nine:
    K -= (num * nine)
    ans += nine

    # 자리수 이동
    num += 1
    nine = nine * 10

# 남은 자리 수의 수를 현재 수에 더해준다.
ans = (ans + 1) + (K - 1) // num

if ans > N:
    print(-1)
else:
    print(str(ans)[(K-1) % num])