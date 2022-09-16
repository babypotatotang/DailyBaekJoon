name = input()
name_info = dict()

for n in name:
    if n not in name_info.keys():
        name_info[n] = name.count(n)

name_info = sorted(name_info.items())

# 팰린드롬 조건 확인: 모든 letter가 짝수 or 하나의 letter만 홀수이면 팰린드롬 
odd_L = ''; odd_n = 0 # 홀수개인 letter 변수, letter의 개수 
for info in name_info:
    if info[1] % 2:
        if odd_L != '':  # odd_L가 발견된 경우 
            print("I'm Sorry Hansoo")
            exit()
        else: odd_L = info[0]; odd_n = info[1]; # update

result = ''; repeat_len = 0

for info in name_info:

    if info[0] != odd_L: # odd_L인 경우 
        result += info[0] * (info[1]//2)
        repeat_len += info[1]//2

    elif info[0] == odd_L and odd_n>1: # odd_L이면서 개수가 1개 이상인 경우 : 사전 정렬을 위해 덧붙여줌
        result += info[0] * (info[1]//2)
        repeat_len +=(info[1]//2)
        odd_n -= (info[1]//2) * 2

result += odd_L * odd_n
result += ''.join(reversed(result[0:repeat_len]))

print(result)