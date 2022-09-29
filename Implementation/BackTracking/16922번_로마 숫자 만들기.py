n = int(input())

nums = [1,5,10,50]
result = []

def track(num_list, depth):
    if depth == n:
        result.append(sum(num_list))
        return 

    for num in nums:
        if num >= num_list[-1]:
            num_list.append(num)
            track(num_list, depth+1)
            num_list.pop()

num_list = []

for num in nums:
    num_list.append(num)
    track(num_list,1)
    num_list.pop()

result = set(result)
print(len(result))    