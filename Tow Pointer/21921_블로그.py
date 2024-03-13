import sys

input = sys.stdin.readline

N, X = map(int, input().split())
visitor = list(map(int, input().split()))
max_v = 0
cnt = 0

if max(visitor) == 0:
    print("SAD")
else:
    cur_value = sum(visitor[:X])
    max_v = cur_value
    cnt = 1

    # 슬라이딩
    for i in range(X, N): # 2부터
        cur_value -= visitor[i - X]
        cur_value += visitor[i]

        if cur_value > max_v:
            max_v = cur_value
            cnt = 1
        elif cur_value == max_v:
            max_v = cur_value
            cnt += 1

    print(max_v)
    print(cnt)