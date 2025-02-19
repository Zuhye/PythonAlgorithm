import sys

input = sys.stdin.readline


E, S, M = map(int, input().split())
# E: 1~15  S: 1~28  M: 1~19
year = 1


while True:
    if((year-E) % 15 == 0) and ((year - S) % 28 == 0) and ((year - M) % 19 == 0):
        break
    year += 1


print(year)
