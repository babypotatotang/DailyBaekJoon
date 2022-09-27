'''
- 연산 1과 연산 2 중 최소 연산 횟수는 무조건 2를 곱했을 때 발생 
- 1을 더한 경우는 홀수의 경우이므로, a를 k로 맞추는 것이 아니라 k를 a로 맞추는 방향으로 진행 
'''
A, k = map(int,input().split())
depth = 0

while 1:
    if A == k: print(depth); break

    if k % 2 == 0 and k >= A*2  : k //= 2
    else: k -=1

    depth +=1 