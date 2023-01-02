import sys
input = sys.stdin.readline

num = 0
while True:
    L, P, V = map(int, input().split())
    num += 1
    if L == 0:
        break
    print(f"Case {num}: {V//P * L + min(L, V%P)}")
