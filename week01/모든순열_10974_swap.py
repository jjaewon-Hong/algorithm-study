# swap방식과 재귀 활용(자료구조) ★사전 방식 출력이 아님을 확인★
# 직접 그린 'permutation_tree.jpg'로 코드 흐름 구조화
# [백준 10974]문제의 정답이 될 수 없어서 '모든순열_10974.py'에 정답 제출함

def perm(data, i, n) :
    if i == n :
        for j in range(n) :
            print(data[j], end=" ")
        print()
        return
    
    else :
        for j in range(i, n):
            data[i], data[j] = data[j], data[i]
            perm(data, i+1, n)
            data[i], data[j] = data[j], data[i]
        
num = int(input())
data_list = [0]*num
for k in range(num) :
    data_list[k] = k+1

perm(data_list, 0, num)