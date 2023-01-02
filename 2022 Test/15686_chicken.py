import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
chicken = []
house = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken.append((i+1, j+1))
        elif city[i][j] == 1:
            house.append((i+1, j+1))

def get_dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

ans = 2*N*len(house) #무한

for combi in combinations(chicken, M):
    total = 0 #도시의 치킨 거리

    for h in house:
       total += min(get_dist(h, chi) for chi in combi) #모든 도시의 치킨거리
    ans = min(ans, total)

print(ans)