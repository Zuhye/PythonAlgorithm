import sys
import math

input = sys.stdin.readline

ax, ay, bx, by, cx, cy, dx, dy = map(int, input().split())

start = 0  # 이동 거리 비율 (0)
end = 100  # 이동 거리 비율 (100)
length = math.sqrt(pow(10000, 2) + pow(10000, 2))  # 최대값

#  절대/상대 오차는 10^-6까지 허용
while end - start >= 1e-7:
    point1 = (start * 2 + end) / 3
    point2 = (start + end * 2) / 3

    minho = [ax + (bx - ax) * (point1 / 100), ay + (by - ay) * (point1 / 100)]
    gangho = [cx + (dx - cx) * (point1 / 100), cy + (dy - cy) * (point1 / 100)]

    minho2 = [ax + (bx - ax) * (point2 / 100), ay + (by - ay) * (point2 / 100)]
    gangho2 = [cx + (dx - cx) * (point2 / 100), cy + (dy - cy) * (point2 / 100)]

    # point1 에서의 민호와 강호 거리
    dist1 = math.sqrt(pow(minho[0] - gangho[0], 2) + pow(minho[1] - gangho[1], 2))

    # point2 에서의 민호와 강호 거리
    dist2 = math.sqrt(pow(minho2[0] - gangho2[0], 2) + pow(minho2[1] - gangho2[1], 2))

    length = min(length, min(dist1, dist2))

    if dist1 >= dist2:
        start = point1
    else:
        end = point2

print('%.10f' % length)
