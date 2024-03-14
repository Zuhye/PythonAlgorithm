import sys
from collections import deque

input = sys.stdin.readline

H, W = map(int, input().split())
block = list(map(int, input().split()))
result = 0

for i in range(1, W-1): # 첫번째 칸과 마지막 칸은 물이 고일 수 없음
    left = max(block[:i]) # 왼 쪽에서 가장 높은 블록
    right = max(block[i+1:]) # 오른 쪽에서 가장 높은 블록

    value = min(left, right) - block[i]
    if value > 0:
        result += value

print(result)
