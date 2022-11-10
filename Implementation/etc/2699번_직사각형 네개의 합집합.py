grid = [[0] * 100 for _ in range(100)]

for _ in range(4): 
    x1, y1, x2 , y2 = map(int,input().split())
    x1 , y1, x2, y2 = x1, y1, x2-1, y2-1 # 오른쪽 위의 꼭짓점은 포함하면 안됨 

    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if not grid[i][j]:
                grid[i][j] = 1

print(sum(sum(grid, [])))