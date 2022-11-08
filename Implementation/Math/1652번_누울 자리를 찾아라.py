N = int(input())

rooms = [list(input()) for _ in range(N)]

# row에서 찾기 
row_cnt = 0
for row in rooms: 
    cnt = 0 # 빈 칸 count 
    for r in row:
        if r == '.': cnt +=1 
        else:
            if cnt>=2: row_cnt +=1 ; cnt = 0 # 누울 수 있다면 cnt 초기화 후 자리 수 +1 
            else: cnt = 0 

    if cnt >=2 : row_cnt += 1; cnt = 0 

# 행열 전환 후 col에서 찾기 
rooms_trans = list(map(list, zip(*rooms)))
col_cnt = 0
for row in rooms_trans: 
    cnt = 0 # 빈 칸 count 
    for r in row:
        if r == '.': cnt +=1 
        else:
            if cnt>=2: col_cnt +=1 ; cnt = 0 # 누울 수 있다면 cnt 초기화 후 자리 수 +1 
            else: cnt = 0 
            
    if cnt >=2 : col_cnt += 1; cnt = 0

print(row_cnt, col_cnt)