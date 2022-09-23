import sys
import heapq

def solve():
    input = sys.stdin.readline

    n,m,k = map(int,input().split())
    beer = [ list(map(int,input().split())) for _ in range(k)]
    beer.sort(key = lambda x: x[1]) # 도수를 기준으로 오름차순 정렬 -> 작은 도수부터 채워나가므로 간 레벨의 최소값을 출력할 수 있음 

    likes = []; hap = 0
    for i in beer:
        if len(likes) < n: # 아직 더 들어가야한다면 
            heapq.heappush(likes, i) # push
            hap+= i[0] # 선호도 합 

            if len(likes) == n: # n의 개수를 채웠다면
                if hap >= m: # m보다 크거나 같을 경우 조건 만족 
                    return i[1] # 가장 큰 도수 반환
                else:
                    hap -= heapq.heappop(likes)[0] # 선호도 

    else:
        return -1

print(solve())