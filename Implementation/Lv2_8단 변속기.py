import sys

input = sys.stdin.readline

numbers = list(map(int, input().split()))
flag = True  # 오르막

if len(numbers) != 8 or (numbers[0] != 1 and numbers[0] != 8):
    print("mixed")

for i in range(1, len(numbers)):
    if numbers[0] == 1:  # 오르막 검사
        if numbers[i] - numbers[i - 1] == 1:
            continue
        else:
            print("mixed")
            exit(0)
    elif numbers[0] == 8:
        if numbers[i - 1] - numbers[i] == 1:
            flag = False
            continue
        else:
            print("mixed")
            exit(0)

if flag == True:
    print("ascending")
else:
    print("descending")

# ---------------------------------

# if numbers == list(range(1, 9)):
#     print("ascending")
# elif numbers == list(range(8, 0, -1)):
#     print("descending")
# else:
#     print("mixed")
