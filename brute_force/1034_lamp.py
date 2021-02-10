import copy
def get_number_of_rowall(bulbs):
    # global var: N, M
    cnt = 0
    for i in range(N):
        if sum(bulbs[i]) == M:
            cnt += 1
    return cnt

def turn_on_col(bulbs):
    # global var: N
    for i in range(N):
        bulbs[i][j] = not bulbs[i][j]

# bulbs0: 원본 전구행렬
N0, M = map(int, input().split())
bulbs0 = [0] * N0
for i in range(N0):
    bulbs0[i] = list(map(int, list(input())))
K = int(input())

# bulbs1: 모두 킬 수 있는 행만 포함한 전구행렬
bulbs1 = []
for i in range(N0):
    n_remained = K - bulbs0[i].count(0)
    if (n_remained < 0) or (n_remained % 2 != 0):
        continue
    bulbs1.append(bulbs0[i])
N = len(bulbs1)

max_rowall = get_number_of_rowall(bulbs1)
if K == 0:
    print(max_rowall)
else:
    for i in range(N): # 각 행별로 스위치를 모두 킨다.
        bulbs = copy.deepcopy(bulbs1) # 실제로 변경하기 위해 깊은복사

        for j in range(M):
            if not bulbs[i][j]:
                turn_on_col(bulbs)
        max_rowall = max(max_rowall, get_number_of_rowall(bulbs))

    print(max_rowall)