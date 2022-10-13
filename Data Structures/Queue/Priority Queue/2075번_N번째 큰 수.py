from heapq import heapify, heappush, heappop
from queue import Empty

N = int(input())
heap = []

for _ in range(N):
    nums = list(map(int,input().split()))

    for num in nums: # push 
            heappush(heap, num) 

    heap = [heappop(heap) for i in range(len(heap))] # 정렬 

    if len(heap) > N:
        while len(heap) != N: 
            heappop(heap)

print(heappop(heap))