import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def find(rowhead, colhead, size):
    global chairs 
    if size == 1:
        return chairs[rowhead][colhead]
    else:
        chair = [find(rowhead,colhead, size//2),find(rowhead, colhead+size//2,size//2), find(rowhead+size//2, colhead, size//2),find(rowhead+size//2, colhead+size//2, size//2)]
        chair.sort()

    return chair[1]

n = int(input())
chairs = []
for _ in range(n):
    chairs.append(list(map(int,input().split())))

print(find(0,0,n))