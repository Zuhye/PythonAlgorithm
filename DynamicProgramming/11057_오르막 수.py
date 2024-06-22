import sys

input = sys.stdin.readline


#  dp 2차원
# 뒤에 숫자 추가
def solution():
    N = int(input())
    dp = [[0] * 10 for _ in range(N + 1)]
    dp[1] = [1] * 10

    for i in range(2, N + 1):
        for j in range(10):
            dp[i][j] = sum(dp[i - 1][j:])

    ans = sum(dp[N])

    return ans % 10007


# -----------------------------------------
# dp 1차원
def solution2():
    N = int(input())
    dp = [1] * 10

    for i in range(2, N + 1):
        for j in range(10):
            dp[j] = sum(dp[j:])

    ans = sum(dp)

    return ans % 10007


# ------------------------------------------
# 앞에 숫자 추가

def solution3():
    N = int(input())
    dp = [1] * 10

    for _ in range(N - 1):
        for j in range(1, 10):
            dp[j] += dp[j - 1]

    ans = sum(dp)
    print(ans % 10007)


solution3()
