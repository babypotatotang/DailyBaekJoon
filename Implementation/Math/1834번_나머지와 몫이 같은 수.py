N = int(input())

x_range = [i for i in range(1, N)]
result = 0
for x in x_range:
    result += N * x + x

print(result)