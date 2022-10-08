import math 

a1, b1 = map(int,input().split())
a2, b2 = map(int,input().split())

# 최소공배수 찾기 
lcm = math.lcm(b1,b2)

# 1과 2에 대한 최소공배수가 되기 위한 몫 구하기
div1 = lcm / b1; div2 = lcm / b2

# 각 몫을 곱해주기
aresult = int(a1*div1 + a2 * div2)
bresult = lcm 

# 최대 공약수 찾기 
gcd = math.gcd(aresult, bresult)

# 기약분수 만들기 
aresult //= gcd; bresult //=gcd

print(f"{aresult} {bresult}") # 결과 출력 