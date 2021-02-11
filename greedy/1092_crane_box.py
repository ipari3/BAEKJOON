# Inputs
N = int(input())
cranes = list(map(int, input().split()))
cranes.sort(reverse=True)

M = int(input())
boxes = list(map(int, input().split()))
boxes.sort(reverse=True)

# each starts at maximum capacity
def bisect_l_rev(w, boxes):
    s, e = 0, M
    while s < e:
        mid = (s + e) // 2
        if boxes[mid] > w:
            s = mid + 1
        else:
            e = mid
    return s

indices = [0] * N
prev_idx = -1
for i in range(N):
    curr_idx = bisect_l_rev(cranes[i], boxes)
    if curr_idx <= prev_idx:
        curr_idx = prev_idx + 1
    indices[i] = curr_idx
    prev_idx = curr_idx

# main
if indices[0] != 0:
    print(-1)
else:
    time = 0
    while True:
        M = len(boxes)
        if M == 0:
            break
        
        N = min(N, M)
        N_tmp = N
        for i in reversed(range(N)):
            idx = indices[i]
            if idx >= M:
                N_tmp -= 1
            else:
                boxes.pop(idx)
                for j in range(i+1, N_tmp):
                    indices[j] = max(indices[j]-1, indices[j-1]+1)
        N = N_tmp
        time += 1
    print(time)