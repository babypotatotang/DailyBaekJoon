input_string = input()
#input_string = '<ab cd>ef gh<ij kl>'
ans = ''; tmp = ''; tag_flag = False

for string in input_string:
    if len(tmp) > 0 and string == '<': 
        ans += tmp[::-1]; tmp = ''

    tmp += string 

    if string == '<': 
        tag_flag = True
    if string == '>': tag_flag = False; ans+=tmp; tmp = ''
    if string == ' ': 
        if not tag_flag:
            tmp = tmp[:-1]
            ans += tmp[::-1] + " "
            tmp = ''

if tmp: ans += tmp [::-1]

print(ans)