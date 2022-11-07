n = int(input())
nums = list(map(int,input().split()))

tmp = [0] * 100001
cnt = 0
ck = False

for i in range(n): # 수가 얼마나 등장했는지 count
    tmp[nums[i]] +=1

for i in range(len(tmp)): # 전체 중에서 등장한 횟수가 가장 많은 값 저장 
    if tmp[i] == i: cnt = i; ck = True

if ck: print(cnt)
else: print(-1)