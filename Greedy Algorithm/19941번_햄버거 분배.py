N, k = map(int,input().split())
line  = list(input())
result = 0 

for index in range(N):
    if line[index] == 'P': # 사람이라면 
        for jindex in range(index-k, index+k+1):
            if 0<=jindex<N: 
                if line[jindex] == "H":
                    line[jindex] = "_" # 먹음
                    result +=1

                    break

print(result)
