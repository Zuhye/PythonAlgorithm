import sys

input = sys.stdin.readline

duck = input().rstrip()
visited = [False] * len(duck)
ans = 0
flag = False
quack = 'quack'
idx = 0

if len(duck) % 5 != 0 or duck[0] != 'q':
    print(-1)
    exit()

for i in range(len(duck)):
    if duck[i] == "q" and not visited[i]:
        flag = True

        for j in range(len(duck)):
            if not visited[j] and quack[idx] == duck[j]:

                visited[j] = True
                if duck[j] == "k":
                    if flag == True: # 한번도 안 울었으면
                        ans += 1 # count 증가하고
                        flag = False # 울었던 전적이 있으니 False로 변경
                    idx = 0
                    continue
                idx += 1


if ans == 0 or not all(visited):
    print(-1)
else:
    print(ans)