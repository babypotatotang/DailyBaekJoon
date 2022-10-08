from itertools import product

n = int(input())
num_list = list(map(int,input().split()))
result = 0 
print(product(num_list,2))

pair_list = product(num_list,2)

for pair in pair_list:
    result += abs(pair[0] - pair[1])

print(result)