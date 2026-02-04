# 1등은 합격 고정 
# 서류 2등부터 N까지는 면접으로 비교
# 서류 순위가 아닌 면접 순위 커트라인을 초기화 하면서 접근
import sys

def solve() :
    T = int(sys.stdin.readline())

    for _ in range(T) :
        N = int(sys.stdin.readline())

        grades = [] 
        for _ in range(N) :
            grades.append(list(map(int, sys.stdin.readline().split())))

        grades.sort()
        # 자동으로 첫번째 요소인 서류 기준으로 정렬함

        cutoff = grades[0][1] # 최초 기준 => 서류 1등의 면접 순위
        count = 1

        for i in range(1, N) : # 어차피 서류는 오름차순 정렬해놓은 상태라 면접만 비교하면 됨
            if grades[i][1] < cutoff : # 면접 커트라인을 높여가는 과정
                count += 1
                cutoff = grades[i][1]
        
        print(count)

solve()



