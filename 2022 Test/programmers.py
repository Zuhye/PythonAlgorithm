def solution(arr1, arr2):
    answer = [[]]
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            answer[i][j] = arr1[i][j] + arr2[i][j]

    print(answer)
solution([[1,2],[2,3]], [[3,4],[5,6]])