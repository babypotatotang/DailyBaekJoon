import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))

result = -1 
array = []

def cal(tmp_array): # 정답을 계산하는 함수 
    ans = 0
    for i in range(N-1):
        ans += abs(tmp_array[i] -tmp_array[i-1])

    return ans

def track(depth, t_nums):
    global result, array
    if depth == N:
        tmp = cal(array)
        result = max(result, tmp)
        return 

    for i in range(len(t_nums)):
        array.append(t_nums[i])

        # 선택할 num의 개수를 축약 
        new_nums = t_nums.copy()
        new_nums.pop(i)

        track(depth+1, new_nums)
        array.pop()

for i in range(N):
    array.append(nums[i])

    # 선택할 num의 개수를 축약 
    t_nums = nums.copy()
    t_nums.pop(i)

    track(1, t_nums)
    array.pop()

print(result)