n = int(input())
H = list(map(int,input().split()))
A = list(map(int,input().split()))

HA = [[H[i], A[i]] for i in range(n)]
HA.sort(key = lambda x: x[1]) # A 값을 기준으로 (나무가 자라는 길이) 오름차순 정렬 
result = 0 

for step in range(0, n):
    result += HA[step][0] + HA[step][1] * step 

print(result)