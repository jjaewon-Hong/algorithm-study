def heap_push(heap, n):
    heap.append(n)
    idx = len(heap) - 1
    while idx > 0:
        parent = (idx - 1) // 2
        if heap[idx] < heap[parent]:
            heap[idx], heap[parent] = heap[parent], heap[idx]
            idx = parent
        else:
            break

def heap_pop(heap):
    if not heap:
        return 0
    if len(heap) == 1:
        return heap.pop()
    
    result = heap[0]
    heap[0] = heap.pop()
    idx = 0
    length = len(heap)
    
    while True:
        left = idx * 2 + 1
        right = idx * 2 + 2
        smallest = idx
        
        if left < length and heap[left] < heap[smallest]:
            smallest = left
        if right < length and heap[right] < heap[smallest]:
            smallest = right
        
        if idx != smallest:
            heap[idx], heap[smallest] = heap[smallest], heap[idx]
            idx = smallest
        else:
            break
            
    return result

n = int(input())
heap = []

for _ in range(n):
    x = int(input())
    if x == 0:
        print(heap_pop(heap))
    else:
        heap_push(heap, x)