import re
# pseudo-pattern: (100+1+ | 01)+
# 1. 전체를 반복하기 위해 둥근괄호로 묶는다. (꺽쇠X)
# 2. (A|B)에서 | 앞뒤를 띄어쓰지 않도록 주의. (띄어쓰기도 포함됨)
p = re.compile("(100+1+|01)+")
n = int(input())
for i in range(n):
    if p.fullmatch(input()):
        print("YES")
    else:
        print("NO")