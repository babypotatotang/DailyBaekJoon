import sys 

n = int(input())

total = [0] * 3 # 전체 점수의 합을 담는 배열
score = [0] * 3 # 전체 점수의 제곱 합을 담는 배열 

for _ in range(n):
    one, two, three = map(int,input().split())
    total[0] += one; total[1] += two; total[2] += three
    score[0] += one**2; score[1] += two**2; score[2] += three**2

if total.count(max(total)) == 1 : # 가장 점수가 높은 후보가 한명일때
    print(total.index(max(total)) + 1, max(total))
    sys.exit()
else: # 가장 점수가 높은 후보가 여러명일 때 
    pow_max = max(score)
    if score.count(pow_max) == 1: # 제곱합 max 가 한명일때 
        print(score.index(pow_max) + 1, max(total))
        sys.exit()

# 찾지 못한 경우 
print(0, max(total))