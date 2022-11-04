people = [0] * 10

for i in range(10): 
    t_out, t_in, = map(int, input().split())

    if i == 0 : people[0] = t_in
    else:
        people[i] = people[i-1] - t_out + t_in

print(max(people))