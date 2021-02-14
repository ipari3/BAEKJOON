N, K = map(int, input().split())
r_N = N % K
if r_N == 0:
    print(1)
else:
    """
    N1 = N(1)            = NG1
    N2 = N(E + 1)        = NG2 = N(G1*E + 1)
    N3 = N(E**2 + E + 1) = NG3 = N(G2*E + 1)
    ...
    N_curr = NG_curr\
    , G_curr = G_prev*E + 1\
    , G_1 = 1
    r_curr = (r_N * r_G_curr) % K\
    , r_G_curr = ((r_G_prev*r_E) % K + 1) % K
    , r_G_1 = 1

    r_G_curr이 반복되면 순환 시작(0이 아님), 나누어 떨어지지 않음
    K에 대한 나머지는 0 ~ K-1이므로,
    K번 반복하면 모든 나머지가 다 나오거나 나머지가 반복됨 (비둘기집 원리)
    """

    r_E = 10**len(str(N)) % K
    r_G = 1
    for cnt in range(2, K+1):
        r_G = ((r_G*r_E) % K + 1) % K
        if (r_N * r_G) % K == 0:
            break
        
    else: # if not found
        cnt = -1
    print(cnt)

##################################################################################
N0, K0 = input().split()
N, K = int(N0), int(K0)
len_N = len(N0)

r_N = N % K
if r_N == 0:
    print(1)
else:
    """
    r_step = N(E**t) % K
           = (N(E**(t-1)) * E) % K
           = (r_step_prev * r_E) % K
    r_curr = (r_prev + r_step) % K
    이 패턴으로는 비둘기집 원리를 도출하기 힘들지만,
    마찬가지로 K번 반복하면 된다.
    """
    r_E = (10**len_N) % K
    r_step, r_curr = r_N, r_N # cnt = 1
    for cnt in range(2, K+1):
        r_step = (r_step * r_E) % K
        r_curr = (r_curr + r_step) % K
        if r_curr == 0:
            break
    else:
        cnt = -1
    print(cnt)