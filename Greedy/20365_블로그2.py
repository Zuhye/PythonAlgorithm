import sys

input = sys.stdin.readline

N = int(input())
colors = input()

dic = {'B': 0, 'R': 0}
dic[colors[0]] = 1

for i in range(1, N):
    if colors[i] != colors[i-1]:
        dic[colors[i]] += 1

print(min(dic['B'], dic['R'])+1)
