# 시간복잡도 : N^2
# Stable -> 버블,삽입은 기존 순서 존중
# Unstable -> 기존 순서 무너질가능성 있음
# ex) 3 3 1 을 생각했을 때 1 3 3 정렬하면 3끼리의 순서는 무너짐

# 선택정렬
# 전체에서 최솟값을 찾아 정해진 위치로 딱 한 번 옮김
# 맨앞부터 차근차근 초기화 하는 방식 (앞 -> 뒤)
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i #최솟값 하나만 찝어냄
        for j in range(i + 1, n):
            if arr[j][0] < arr[min_idx][0]: 
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# 버블정렬
# 옆에 있는 값과 비교하며 큰 값을 계속 뒤로 밀어냄
# 01 12 23 (가장 큰값 맨뒤로 밀려나 확정) -> 01 12 -> 01 (가장 작은 값이 맨 마지막에 확정) 
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j][0] > arr[j + 1][0]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 삽입정렬 (시간복잡도 N^2에도 불구하고 실무에서 종종 사용)
# 정렬된 줄 사이에 내 자리 찾아 끼어듬
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j][0] > key[0]: 
            # arr[i] 기준으로 자신보다 더 작은게 뒤에 없으면 while문 탈출 
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key #모든 정렬 이후에 앞에서 하나씩 값을 넣음

    return arr
