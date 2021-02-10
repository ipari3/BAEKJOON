import operator
from functools import reduce
from itertools import combinations

def nCr(n, r):
    r = min(r, n-r)
    numer = reduce(operator.mul, range(n, n-r, -1), 1) # n-r을 포함하지 않음
    denom = reduce(operator.mul, range(1, r+1), 1) # r을 포함해야 하므로 r+1
    return numer // denom

N = int(input())

if N < 10: # 1 ~ 9
    print(N)
else:
    cnt = 9 # 1 ~ 9 = 9개
    down = False # up/down 게임

    # 10 ~ 9876543210
    for i in range(1, 10): # (i+1) 자리수, i = 자리수-1
        for j in range(i, 10): # j = first digit, 최대 9
            cnt += nCr(j, i) # 둘째자리부터의 조합수, 0을 포함하므로 j
            if cnt >= N:
                down = True
                break
        if down:
            break
    if down:
        cnt -= nCr(j, i)
        combs = sorted(list(combinations(range(j), i)),
                       key=lambda x: tuple(x[i] for i in reversed(range(i)))
                      )
        rem = N - cnt
        print(int( str(j) + "".join(map(str, reversed(combs[rem-1]))) ))
    else:
        print(-1) # 9876543210보다 큰 수는 감소하는 수가 될 수 없음