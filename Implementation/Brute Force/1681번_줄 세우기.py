n, m = map(int,input().split())
dp = []
index = 1

while(1):
    if str(m) not in str(index):
        dp.append(index)

    index+=1

    if len(dp) == n:
        print(dp[n-1])
        break