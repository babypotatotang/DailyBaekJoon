col = int(input())
string = input(); total = len(string); 
row = total//col

res = []

for i in range(row):
    tmps = string[i*col:(i*col)+col]
    
    if i%2 : # 홀수라면 
        tmps = tmps[::-1]
    
    res.append(list(tmps))

for c in range(col):
    for r in range(row):
        print(res[r][c],end = '')