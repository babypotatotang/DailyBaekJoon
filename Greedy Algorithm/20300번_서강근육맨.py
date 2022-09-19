import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
muscle = deque(sorted(list(map(int,input().split()))))

M = muscle.pop() if N%2 else int(1e9)
while muscle: M = max(M, muscle.pop() + muscle.popleft())

print(M)