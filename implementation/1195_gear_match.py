gear = [0, 0]
gear[0] = input()
gear[1] = input()

length = [len(gear[0]), len(gear[1])]
longer_length = max(length)
answer = sum(length)
def find_min_length(m, n, answer):
    # i는 m기어의 뒤에서부터 앞으로 이동(감소)
    # j는 m기어와 n기어가 한 개씩 맞물리도록 증가
    for i in reversed(range(length[m])):
        for j in range(length[m]-i):
            if ((i + j) < length[m]) and (j < length[n])\
            and (gear[m][i+j] == "2") and (gear[n][j] == "2"):
                break # 두 이가 만나면 실패
        else:
            rear_length_n = length[n] - length[m] + i # n기어가 튀어나온 길이
            if rear_length_n > 0:
                answer = min(answer, length[m] + rear_length_n)
            else:
                answer = longer_length # 최소 맞물린 길이
                return 1, answer
    return 0, answer

done, answer = find_min_length(0, 1, answer)
if done:
    print(answer)
else:
    _, answer = find_min_length(1, 0, answer)
    print(answer)