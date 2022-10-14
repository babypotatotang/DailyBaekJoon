result = []
for _ in range(7):
    num = int(input())

    if num % 2: 
        result.append(num)

if result: 
    print(sum(result))
    print(min(result))
else:
    print(-1)