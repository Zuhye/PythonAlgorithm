import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9) # 파이썬의 재귀 최대 깊이 설정

N, M = map(int, input().split())

root = {}

for i in range(N + M):
    P, F, C = map(str, input().split())
    if P not in root:
        root[P] = []
    root[P].append((F, C))


def folder(name, file_type):
    global file_cnt

    if name not in root:
        return
    else:
        for f in root[name]:
            if f[1] == "0" and f[0] not in file_type:
                file_type.add(f[0])
                file_cnt += 1
            elif f[1] == "0" and f[0] in file_type:
                file_cnt += 1
            else: # 폴더 일 때 -> 재귀
                folder(f[0], file_type)
    return


Q = int(input())
for i in range(Q):
    cnt = 0
    location = input().rstrip().split("/")
    file_type = set()
    file_cnt = 0
    folder(location[-1], file_type)
    print(len(file_type), file_cnt)
