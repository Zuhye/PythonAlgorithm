data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]


def quick_sort(data):
    if len(data) <= 1:
        return data

    # 피벗으로 리스트의 첫 번째 요소를 사용

    pivot = data[0]

    left, right, same = [], [], 0

    for i in data:
        if i < pivot:
            left.append(i)  # 피벗보다 작은 요소는 왼쪽으로 이동

        elif i > pivot:
            right.append(i)  # 피벗보다 큰 요소는 오른쪽으로 이동

        else:
            same += 1

    left = quick_sort(left)  # 왼쪽을 정렬
    right = quick_sort(right)  # 오른쪽을 정렬

    # 정렬 결과와 피벗 값을 함께 반환
    return left + [pivot] * same + right


print(quick_sort(data))
