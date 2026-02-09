import sys

def solve() :
    N = int(sys.stdin.readline()) # 사진틀의 개수
    M = int(sys.stdin.readline()) # 학생의 총 추천 횟수
    recommend = list(map(int, sys.stdin.readline().split())) # 추첨 결과
    
    world_best = [0] * 101
    final = []

    # N 순위까지 점수 높은 후보들 순서 없이 추려내는 과정
    # 점수가 같다면 최신 순
    for student in recommend : 
        if student in final: # 이미 사진틀에 있는 학생인 경우
            world_best[student] += 1 # 학생 교체 필요없이 점수만 +1
        else : # 사진틀이 꽉 찬 경우
            if len(final) >= N : 
                target_student = final[0] # 가장 먼저 들어온 값을 가리킴 (임시 타겟)
                min_score = world_best[target_student] # 현재 들어갈 학생의 점수

                for f in final : # 현재 사진틀 다 탐색
                    if world_best[f] < min_score : 
                        # world_best에 현재 학생 점수보다 낮은애가 있다면 그 애가 삭제할 타겟 
                        min_score = world_best[f] # 최저 점수 기준 바꿈
                        target_student = f 
            
                final.remove(target_student)
                world_best[target_student] = 0

            # 빈자리가 생겼거나 원래 자리 있는 경우 => 사진 틀에 추가
            final.append(student)
            world_best[student] = 1

    final.sort() # 후보 애들은 뽑았고 문제 조건 맞춰 오름차순 정렬
    for i in final :
        print(i, end = " ")

solve()

