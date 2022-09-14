a, b = map(int,input().split())
A = sorted(list(map(int,input().split())), reverse=True) # 내림차순 정렬
B = sorted(list(map(int,input().split())), reverse = False) # 오름차순 정렬
result = 0

n = min(a,b) # 둘 중에 작은 값을 기준으로 for문 돌리기 

for i in range(n):
    val = A[i] - B[i] # 고객 만족도
    if val>=0: result +=val # 고객만족도가 0 이상인 경우에만 더하기 

print(result)