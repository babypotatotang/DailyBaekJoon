s = input()

slist = sorted([s[i:len(s)] for i in range(0,len(s)+1)])

for i in range(1,len(slist)):
    print(slist[i])