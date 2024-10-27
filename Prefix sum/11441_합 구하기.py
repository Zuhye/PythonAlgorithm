import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
ranges = [list(map(int, input().split())) for _ in range(M)]

prefix = [0] * (N + 1)
for i in range(1, N + 1):
    prefix[i] = prefix[i - 1] + nums[i - 1]

for i in ranges:
    s, e = i
    print(prefix[e] - prefix[s - 1])