import sys 
input = sys.stdin.readline

def track(result, depth):
    if depth == 6:
        for r in result:
            print(r, end = ' ')
        print()
        return 

    for a in array:
        if (depth == 0) or (a > result[-1]):
            result.append(a)
            track(result, depth+1)
            result.pop()

while(1):
    array = list(map(int,input().split()))
    if array[0] == 0 : break
    
    array =  array[1:]
    array.sort()

    result = []
    track(result, 0)