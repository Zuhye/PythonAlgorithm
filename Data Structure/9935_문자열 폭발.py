import sys

input = sys.stdin.readline

inputs = str(input().rstrip())
bomb = str(input().rstrip())
results = []


def find(idx):
    if len(bomb) == idx: # 폭탄 찾으면 True
        return True
    if len(results) < len(bomb):
        return False
    if bomb[-idx - 1] == results[-idx - 1]:
        return find(idx + 1)


for i in inputs:
    results.append(i)
    if find(0):
        for _ in range(len(bomb)):  # 폭탄 길이 만큼 제거
            results.pop()
if results:
    print(''.join(results))
else:
    print("FRULA")
