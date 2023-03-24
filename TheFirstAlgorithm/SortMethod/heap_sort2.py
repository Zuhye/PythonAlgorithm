data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]


def heapify(data, i):
    left = 2 * i + 1  # 왼쪽 아래의 위치
    right = 2 * i + 2  # 오른쪽 아래의 위치
    size = len(data) - 1
    min = i

    if left <= size and data[min] > data[left]:
        min = right

    if right <= size and data[min] > data[right]:
        min = right

    if min != i:  # 교환이 발생하는 경우
        data[i], data[min] = data[min], data[i]
        heapify(data, min)  # 힙을 재구성


# 정렬 실행
sorted_data = []

for _ in range(len(data)):
    data[0], data[-1] = data[-1], data[0]  # 마지막 노드와 맨 앞 노드를 교체
    sorted_data.append(data.pop())  # 최솟값인 노드를 꺼내 정렬된 상태로 표시
    print(sorted_data)
    heapify(data, 0)  # 힙을 재구성

print(sorted_data)

# 힙 구성
for i in reversed(range(len(data) // 2)):  # 리프 노드 이외를 처리
    heapify(data, i)
