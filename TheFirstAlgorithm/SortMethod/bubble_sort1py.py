data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]


for i in range(len(data)):
    for j in range(len(data)-i-1): # 정렬된 부분을 제외하고 반복 실행
        if data[j] > data[j+1]:
            data[j], data[j+1] = data[j+1], data[j]

print(data)