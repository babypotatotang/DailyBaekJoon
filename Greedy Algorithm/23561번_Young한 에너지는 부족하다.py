n = int(input())
members = sorted(list(map(int,input().split()))) # 정렬
print(members[2*n-1] - members[n]) 