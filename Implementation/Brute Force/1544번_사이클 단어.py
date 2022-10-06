n = int(input())
word_list = [input() for _ in range(n)]; check_index=[]
result = n

for i in range(n):
    word_i = word_list[i]
    for j in range(i+1,n):
        word_j = word_list[j]

        for _ in range(len(word_j)):
            word_j = word_j[1:] + word_j[0]

            if word_j == word_i and j not in check_index: result -=1; check_index.append(j)

print(result)
        