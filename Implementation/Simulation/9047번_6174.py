import sys 
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = input()

    cnt = 0
    while(1):
        if int(n) == 6174: print(cnt); break 
        minn = ''.join(sorted(n))
        maxn = ''.join(sorted(n,reverse = True))

        n = str(int(maxn) - int(minn))
        cnt+=1

        if len(n) < 4: 
            zeros = '0' * (4-len(n))
            n = zeros + n