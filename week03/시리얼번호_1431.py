# [조건]
# 1. 길이 짧은거 먼저 출력
# 2. 길이 같으면 숫자만 골라서 다 더했을때 작은거 먼저 출력
# 3. 길이도 같고 숫자만 골라 더한것도 같으면 사전순 출력

import sys
def cmp3(x,y) :  # 문자열 끼리 <,> 사용하면 알아서 사전순 비교
    return x > y   # 맞으면 True, 틀리면 Fasle 반환
 
def cmp2(x, y): # 숫자만 골라서 다 더한후 비교
    total1 = 0
    for item in x:
        if '0' <= item <= '9':
            total1 += int(item)
    
    total2 = 0
    for item in y:
        if '0' <= item <= '9':
            total2 += int(item)
            
    if total1 > total2:
        return True
    elif total1 < total2:
        return False
    else:
        return cmp3(x, y)

def cmp1(x, y): # 배열의 길이 비교
    if len(x) > len(y): 
        # 배열에 들어있는 요소의 길이를 비교
        # len(arr)은 배열의 수 
        # len(arr[j]), len(x)는 한줄에 있는 각각 배열의 길이
        return True
    elif len(x) < len(y):
        return False
    else:
        return cmp2(x, y)
    
line = sys.stdin.readline() # 몇줄 받을지 입력받음
if line:
    n = int(line)
    arr = []
    for _ in range(n):
        arr.append(sys.stdin.readline().strip()) #arr에 모든 요소가 담겨짐

    for i in range(len(arr)): 
        for j in range(len(arr) - 1 - i): 
            # i가 0일때 부터 가장 큰 수는 위치가 맨뒤로 정해지므로 -i씩 빼줘 효율을 높임
            if cmp1(arr[j], arr[j+1]): 
                # cmp동작 통해 뒤보다 앞이 더 큰 애들만 True로 받아놨기 때문에 스왑
                arr[j], arr[j+1] = arr[j+1], arr[j]

    for result in arr:
        print(result)




    

    