# 먼저 요청 값들의 합이 예산액으로 해결되는지를 판별
# 해결되면 요청 값들 중 최대값, 안되면 상한값 찾아내야 함

import sys

def search_Maximum(M, money_list) : # M: 총예산, total_request: 총 요청액
    total_request = sum(money_list) # sum 함수땜에 N 굳이 인자로 받을 필요 없어짐

    if total_request <= M :
        return max(money_list)
    else :
        low = 0
        high = max(money_list)
        answer = 0

    #-------이분탐색의 기본적인 형태 --------------------------------------
        while low <= high:
            ceiling = (low + high) // 2 # 가상의 천장 -> ceiling
            
            current_sum = 0
            for i in money_list : 
                if i > ceiling : 
                    current_sum += ceiling # 천장 뚫으면 천장까지만 줘라
                else :
                    current_sum += i # 천장 안뚫으면 다 줘라
            
            # +1과 -1은 단순히 한 칸 움직이는 게 아니라, 
            # 이미 확인한 ceiling 값을 다음 탐색 범위에서 깔끔하게 제외하기 위한 장치

            if current_sum <= M : # 예산안 작거나 같은 경우
                answer = ceiling
                low = ceiling + 1 
                # low를 초기화 시켜 작은 값 다 쳐냄 +1 통해 아래 깎아내며 결과 미세 조정
            else : # 예산안 넘는 경우
                high = ceiling - 1 
                # high를 초기화 시켜 더 큰 값 다 쳐냄 -1 통해 위쪽 깎아내며 결과 미세 조정
            
        return answer
    #---------------------------------------------------------------------
    
N = int(sys.stdin.readline())
money_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

print(search_Maximum(M, money_list))