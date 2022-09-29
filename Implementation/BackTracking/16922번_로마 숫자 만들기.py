n = int(input())

nums = [1,5,10,50] # 사용할 숫자들 
result = []

def track(num_list, depth):
    if depth == n: # 깊이가 주어진 n과 같다면 
        result.append(sum(num_list)) # 결과에 합을 넣고 
        return # 반환 

    for num in nums:
        if num >= num_list[-1]: # 크거나 같은 숫자에 대해서 append 
            num_list.append(num)
            track(num_list, depth+1)
            num_list.pop()

num_list = []

for num in nums:
    num_list.append(num)
    track(num_list,1)
    num_list.pop()

result = set(result) # 중복 제거 후
print(len(result))   # 결과 개수 반환 