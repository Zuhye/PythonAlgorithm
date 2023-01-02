from collections import Counter

# c = Counter(input())
c = dict() #'A':2 (알파벳문자: 사용된 갯수)
name = input()

for i in name:
    if i in c:
        c[i] +=1
    else:
        c[i] = 1

if sum(i % 2 for i in c.values()) >1: #다 더하면 홀수개의 갯수가 나옴
    print("I'm Sorry Hansoo")
else:
    half = ''
    for k, v in sorted(c.items()):
        half += k*(v//2)
    ans = half
    for k, v in c.items():
        if v%2 != 0:
            ans += k
            break
    ans += ''.join(reversed(half))
    print(ans)