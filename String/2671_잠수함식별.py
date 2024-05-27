import sys
import re # 정규 표현식

input = sys.stdin.readline
N = str(input().rstrip("\n"))

pattern = re.compile('(100+1+|01)+')

if pattern.fullmatch(N):
    print("SUBMARINE")
else:
    print("NOISE")