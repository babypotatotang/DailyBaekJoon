from collections import deque

N = int(input())
muscle = deque(sorted(list(map(int,input().split())))) # 오름차순 정렬
 
M = muscle.pop() if N%2 else int(1e9) # N이 짝수, 홀수인 경우에 나눠서 M 선언 
while muscle: M = max(M, muscle.pop() + muscle.popleft()) # max M 찾기 

print(M)