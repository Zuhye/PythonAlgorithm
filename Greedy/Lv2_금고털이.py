import sys

input = sys.stdin.readline

W, N = map(int, input().split())
metal = []  # (무게, 가격)

for i in range(N):
    m, p = map(int, input().split())
    metal.append([m, p])

metal.sort(key=lambda x: x[1], reverse=True)

prices = 0
for weight, price in metal:
    if W == 0:
        break

    if weight <= W:
        W -= weight
        prices += weight * price  # 가격
    else:
        prices += W * price
        W = 0

print(prices)