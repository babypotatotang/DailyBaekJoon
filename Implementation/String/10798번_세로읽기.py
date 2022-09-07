text = [list(input()) for _ in range(5)]
s = ''
for i in range(15):
    for j in range(5):
        try:
            s+=text[j][i]
        except:
            continue

print(s)