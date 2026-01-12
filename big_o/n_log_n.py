# 시간복잡도 : NlogN, 퀵은 최악일때 N^2인 경우도 있음
# Stable -> 병합은 기존 순서 보장
# Unstable -> 퀵, 힙
# 힙 정렬을 기본으로 빠른걸 원하면 퀵(피봇), 메모리 여유있으면 병합  

# 병합정렬
# 일단 반으로 쪼개고 본다 (쪼갤 수 없을 때까지) -> 그 다음 합치면서 정렬
# 시간복잡도 : 반으로 자르는 재귀동작이 logN이고 while문이 N 이다 
# 근데, 그걸 더하지 않고 곱한 이유가 while문 자체가 logN된 상태를 다룬거기 때문에 NlogN
def merge_sort(arr): 
    if len(arr) < 2:
        return arr

    #쪼개는 동작
    # ex) 3142 좌좌3, 돌아오며 우1, 돌아오며 우좌4, 돌아오며 우2, 돌아옴, 돌아옴
    mid = len(arr) // 2 
    low_arr = merge_sort(arr[:mid]) 
    # mid기준 왼쪽 묶어둬라 
    high_arr = merge_sort(arr[mid:])
    # mid기준 오른쪽 묶어둬라
     
    merged_arr = []
    l = h = 0
    # len(low_arr)과 l의 크기는 계속 한개씩 차이나면서 큰 기준 왼쪽 배열이 다 담겨지는 형태
    while l < len(low_arr) and h < len(high_arr): 
        if low_arr[l][0] <= high_arr[h][0]: 
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    
    # low_arr나 high_arr에 담겨져에 담겨있는 깍두기 하나 처리 ( 이미 처리된 쪽의 뒤쪽 -> [l:] )
    # 가장 큰수가 최초에 mid 기준 좌측이었으면 merged_arr += low_arr[l:]만 동작함
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr

# 퀵정렬 = 피봇 정렬
# 기준(Pivot)을 하나 잡고, 걔보다 작은 건 왼쪽, 큰 건 오른쪽으로 몰아넣음
# 분할 정복(Divide and Conquer)의 대표적인 예시 -> 병합정렬과 달리 쪼갤 때 이미 분류해버림
# 데이터가 무작위일 때 가장 빠르고 이미 정렬된 데이터에서 최악의 성능(N^2) 
# 이미 정렬된 경우는 중간값을 피벗으로 잡거나 or 셔플
def quick_sort(arr): #27351
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2] # 중앙값을 피벗으로 설정
    less_arr, equal_arr, big_arr = [], [], []
    
    for num in arr: # for문 N
        if num[0] < pivot[0]: 
            less_arr.append(num) # 2 1
        elif num[0] > pivot[0]:  
            big_arr.append(num) # 7 5
        else:
            equal_arr.append(num) # 3
            
    return quick_sort(less_arr) + equal_arr + quick_sort(big_arr) # 재귀 logN
    # less_arr내에서 또 less equal big으로 나뉘어서 자기들끼리 정리하고 다시돌아오고 
    # quick_sort(less_arr) 출력하고 뒤에 있는 애들도 같은 방식으로 진행

# 힙정렬 
# 최대 힙 기준으로 index하나 잡아서 앞뒤 비교하고 맨뒤로 갈때까지 재귀
def heapify(unsorted, index, heap_size):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    
    # 나머지는 순서 상관없이 가장 큰 값을 스택의 맨 위로 둠
    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index
        
    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index
        
    if largest != index:
        unsorted[index], unsorted[largest] = unsorted[largest], unsorted[index]
        heapify(unsorted, largest, heap_size)

def heap_sort(unsorted): 
    n = len(unsorted)
    
    # unsorted[0]에 가장 큰 값 위치 시킴
    for i in range(n // 2 - 1, -1, -1): 
        heapify(unsorted, i, n)
        
    # unsorted[0]에 있던 값을 맨 끝자리로 보내고 다음 큰값 찾아내기 위해 앞의 과정을 반복
    # for문안에 재귀를 불러오는 방식으로 NlogN    
    for i in range(n - 1, 0, -1):
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        heapify(unsorted, 0, i)
        
    return unsorted