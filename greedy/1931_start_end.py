N = int(input())
# 정렬해야하므로, generator를 사용할 수 없다.
# map(int, input())는 세트
table = []
for i in range(N):
    table.append(list(map(int, input().split(' '))))
# 정렬 기준을 tuple로 묶을 수 있다.
# 내림차순은 -x[0]과 같이 -를 붙여준다.
# 가장 일찍 끝나는 시간부터 greedy하게
table.sort(key=lambda x: (x[1], x[0])) # end, start
count = 0
time = 0
for s, e in table:
    if s < time:
        continue
    count += 1
    time = e

print(count)