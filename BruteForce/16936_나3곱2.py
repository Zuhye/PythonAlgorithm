import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
answer = []

for i in range(N):
    stack = [[nums[i]]]

    while stack:
        temp = stack.pop()  # 스택에서 현재 수열을 가져옴

        if len(temp) == N:
            answer = temp
            break

        for j in nums:
            if j not in temp:
                if temp[-1] * 2 == j:
                    stack.append(temp + [j])

                if temp[-1] == j * 3:
                    stack.append(temp + [j])

print(*answer)