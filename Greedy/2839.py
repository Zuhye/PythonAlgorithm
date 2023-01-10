# 첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000)

N = int(input())
result = 0
while N >= 0:
    if N % 5 == 0:
        result += N//5 #5로 나누어질 떄
        print(result)
        break
    N -= 3
    result += 1
else:
    print(-1)