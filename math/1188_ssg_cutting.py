N, M = map(int, input().split()) # 1 ~ 100, 소시지/평론가
ssg = N % M # 나머지 소시지

def GCD(a, b):
    if a < b:
        a, b = b, a
    r = a % b
    while r:
        a = b
        b = r
        r = a % b
    return b
if not ssg:
    print(0)
else:
    # 소시지를 일렬로 늘어놓고
    # 평론가수만큼 등분 = 평론가수-1번 컷팅
    #
    # GCD로 정규화하여 생각
    # (M_norm - 1)GCD = M - GCD
    print(M - GCD(M, ssg))