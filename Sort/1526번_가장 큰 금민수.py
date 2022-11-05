from itertools import product
import sys 

N = int(input())

nums = ['4','7']
result = 0; tmp = 0; chk = False

for i in range(1, len(str(N))+1):
    # 1부터 주어진 N까지 길이에 해당하는 수 생성 
    cases = [int(''.join(combi)) for combi in product(nums, repeat = i)]

    if max(cases) < N: # 해당 cases에는 없을 수 있음. 
        tmp = max(cases)
    if N in cases: # N이 cases에 있는 경우 
        print(N); sys.exit()
    if max(cases) > N: # 가장 큰 case가 N보다 큰 경우 : 전체 for문으로 돌려서 확인 
        cases = sorted(cases, reverse = True)
        for case in cases:
            if case < N:
                print(case)
                chk = True
                sys.exit()

if not chk: 
    result = tmp

print(result)