input_string = input()
result = [0] * 26

for s in input_string:
    result[ord(s)-97] +=1

print(*result)
