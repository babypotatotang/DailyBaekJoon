def diff(num_array):
    new_array = []

    for i in range(len(num_array)-1):
        new_array.append(num_array[i+1]- num_array[i])


    return new_array


N, K = map(int,input().split())
nums = list(map(int,input().split(',')))

for _ in range(K):
    nums = diff(nums)

nums_str = list(map(str, nums))

print(",".join(nums_str))