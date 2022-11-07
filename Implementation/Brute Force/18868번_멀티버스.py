M, N = map(int,input().split())

spaces = [list(map(int, input().split())) for _ in range(M)]
K = 0

spaces_index = [[space.index(s) for s in sorted(space)] for space in spaces]

for A in range(M-1):
    for B in range(A+1, M):
        if spaces_index[A] == spaces_index[B]: K+=1

print(K)