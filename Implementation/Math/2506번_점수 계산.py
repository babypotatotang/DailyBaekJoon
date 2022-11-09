N = int(input())
res = list(map(int,input().split()))

total_score = 0 
tmp_score = 0 

for r in res:
    if r == 0 : 
        total_score += sum([i for i in range(1,tmp_score+1)])
        tmp_score = 0 
    else:
        tmp_score += 1

if tmp_score : 
    total_score += sum([i for i in range(1,tmp_score+1)])
    
print(total_score)