from collections import deque
import sys

input = sys.stdin.readline
N = int(input())


def solution():
    dp = [[0] * 3 for _ in range(N)]
    dp[0] = [1, 1, 1]
    for i in range(1, N):
        dp[i][0] = sum(dp[i - 1]) % 9901
        dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % 9901
        dp[i][2] = (dp[i - 1][0] + dp[i - 1][1]) % 9901

    print(sum(dp[N - 1]) % 9901)


def solution2():

    # 변수를 사용해서 우변에서 한변에 연산 후 튜플로 받음
    n0 = n1 = n2 = 1
    for i in range(1, N):
        n0, n1, n2 = (n0 + n1 + n2) % 9901, (n0 + n2)% 9901, (n0 + n1)% 9901
    ans = n0 + n1 + n2
    print(ans % 9901)


solution()
solution2()