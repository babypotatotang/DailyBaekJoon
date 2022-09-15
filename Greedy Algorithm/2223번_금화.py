t , x, m = map(int,input().split())
monsters = []
cnt = 0; result = 0

for _ in range(m):
    monsters.append(list(map(int,input().split())))

monsters.sort(key = lambda x: x[0]/x[1]) # 단위 시간 기준으로 오름차순 정렬
minunit = monsters[0][0] / monsters[0][1] # 가장 작은 값을 unit으로 설정 

for _ in range(t):
    if minunit <= 1: 
        minunit+=1
        continue
    else:
        result += x
        minunit-=1

if m == 0: print(t*x)
else:
    print(result if minunit>1 else 0)