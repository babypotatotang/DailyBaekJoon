import sys 

def diff(line):
    global code_dict
    diffs = []; min_diff = 7; min_letter = ''
    for letter, code in code_dict.items():
        d = 0
        for i in range(6):
            if code[i] != line[i]:
                d+=1 

        if min_diff > d:
            min_letter = letter
            min_diff = d

        diffs.append(d)
    
    if diffs.count(min_diff) >= 2:
        return False
    else:
        return min_letter

code_dict = {
    'A': '000000',
    'B': '001111', 
    'C': '010011',
    'D': '011100', 
    'E': '100110', 
    'F': '101001', 
    'G': '110101',
    'H': '111010'
}

n = int(input())
line = input()
lines = [line[i*6: (i+1)*6] for i in range(n)]
res = ''

for i in range(n):
    if diff(lines[i]):
        res += diff(lines[i])
    else:
        print(i)
        sys.exit()

print(res)
        