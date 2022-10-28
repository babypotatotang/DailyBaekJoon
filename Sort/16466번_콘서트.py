import sys 

N = int(input())
M = list(map(int,input().split()))
M = sorted(M)

if 1 not in M: # 첫번째 자리가 남은 경우 
    print(1); sys.exit()
else:
    for i in range(1,N):
        if M[i] - M[i-1] > 1: # 차이가 1 이상 나는 경우 
            print(M[i-1]+1) # i-1 에서 1을 더한 수 출력 
            sys.exit()

# 중간에 남는 자리가 없는 경우 
print(N+1)