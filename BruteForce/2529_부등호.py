import sys

input = sys.stdin.readline

k = int(input())
sign = list(input().split())

visited = [0] * 10
max_value = ""
min_value = ""


def check(i, j, k):
    if k == "<":
        return i < j
    else:
        return i > j


def solution(length, s):
    global max_value, min_value

    if length == k + 1:  # 맨 처음 생성
        if len(min_value) == 0:
            min_value = s
        else:
            max_value = s
        return

    for i in range(10):
        if not visited[i]:
            if length == 0 or check(s[-1], str(i), sign[length - 1]):
                visited[i] = True
                solution(length + 1, s + str(i))
                visited[i] = False


solution(0, "")
print(max_value)
print(min_value)
