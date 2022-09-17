import sys
input = sys.stdin.readline

n = int(input())
numlist = sorted([int(input()) for _ in range(n)])

while(1):
    try:
        a = numlist[-1]; b = numlist[-2]; c = numlist[-3]

        if a < b+c: print(a+b+c); break
        else:
            numlist.pop()
    except:
        print(-1)
        break