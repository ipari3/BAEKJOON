import sys

N = int(sys.stdin.readline()) # 'N'umber
M = int(sys.stdin.readline()) # 'M'alfunction count
broken_btns = set(sys.stdin.readline().split())

diff = abs(N - 100) # maximum answer
answer = diff
if (M == 10) or (answer == 0): # all-broken or N == 100
    pass
elif M == 0:
    answer = min(answer, len(str(N)))
else:
    # lbound = N - diff + 1
    for under in reversed(range(N-diff+1, N+1)):
        for digit in str(under):
            if digit in broken_btns:
                break
        else:
            answer = min(answer, N - under + len(str(under)))
            break
 
    ubound = N + answer
    for over in range(N+1, ubound):
        for digit in str(over):
            if digit in broken_btns:
                break
        else:
            answer = min(answer, over - N + len(str(over)))
            break
        
print(answer)