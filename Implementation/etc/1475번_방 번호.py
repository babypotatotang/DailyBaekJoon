n = input()
n_count = [n.count(str(i))for i in range(10)]

if n_count[6]%2: n_count[6] = n_count[6] //2 + 1 
else: n_count[6] = n_count[6]//2

if n_count[9]%2: n_count[9] = n_count[9] //2 + 1 
else: n_count[9] = n_count[9]//2


if max(n_count) <= 1:
    print(1)
else:
    print(max(n_count))