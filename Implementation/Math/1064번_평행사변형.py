import math 

ax, ay, bx,by, cx, cy = map(int,input().split())

# AB가 한 변일 경우 
line_ab = math.sqrt((ax-bx)**2 + (ay-by)**2)
line_ac = math.sqrt((ax-cx)**2 + (ay-cy)**2)

max_line = max(line_ab, line_ac)

line_cross = math.sqrt((max_line)**2 + (line_ac)**2)


perimeter_a = max_line*2 + line_ac*2
perimeter_b = line_ab*2 + line_cross*2

if perimeter_a > perimeter_b: 
    print(perimeter_a-perimeter_b )
else:
    print(perimeter_b-perimeter_a )