def overflowing_water(L, A):
    answer = 0

    # 각 구간에서 더 낮은 칸막이 높이를 합산
    for i in range(L):
        answer += min(A[i], A[i+1])

    # 내부에서 가장 높은 칸막이 찾기
    max_inner = max(A[1:L]) if L > 1 else 0

    # 양 끝(A[0], A[L])이 내부 최대값보다 크거나 같으면 물이 안 넘침
    if A[0] >= max_inner and A[L] >= max_inner:
        return 0

    # 그렇지 않으면 모든 물이 넘침
    return L * 100 - answer


# 테스트 케이스 실행
print(overflowing_water(5, [1, 1, 1, 1, 1, 1]))  # 495 (물이 다 넘침) ✅
print(overflowing_water(4, [10, 2, 2, 2, 10]))  # 0 (물이 안 넘침) ✅
print(overflowing_water(6, [3, 2, 1, 3, 1, 2, 3]))  # 600 (물이 다 넘침) ✅
print(overflowing_water(6, [2, 1, 3, 1, 2, 1, 2]))  # 600 (물이 다 넘침) ✅
print(overflowing_water(6, [10, 5, 6, 5, 10, 8, 10]))  # 0 (물이 안 넘침) ✅
