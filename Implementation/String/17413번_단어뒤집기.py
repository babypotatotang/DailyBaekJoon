input_string = input()
ans = ''; tmp = ''; tag_flag = False

for string in input_string:
    if len(tmp) > 0 and string == '<': # tmp에 값이 들어있는데 tag가 시작된다면 
        ans += tmp[::-1]; tmp = '' # ans에 tmp 값을 뒤집어서 append하고, tmp 초기화 

    tmp += string # tmp에 string 더하기 
 
    if string == '<': # tag가 시작됐다면 
        tag_flag = True # tag flag on 
    if string == '>': tag_flag = False; ans+=tmp; tmp = '' # tag가 끝나면, ans에 문자열 append하고 초기화
    if string == ' ': # 공백이라면
        if not tag_flag: # tag안에 있는게 아니라면, 뒤집어서 ans에 append
            tmp = tmp[:-1]
            ans += tmp[::-1] + " "
            tmp = ''

# 공백 또는 tag 신호가 없어서 남아있는 tmp의 경우 ans에 뒤집어서 append 
if tmp: ans += tmp [::-1]

print(ans)