# Preprocessing
all_digits = []
all_digits.append("###...#.###.###.#.#.###.###.###.###.###")
all_digits.append("#.#...#...#...#.#.#.#...#.....#.#.#.#.#")
all_digits.append("#.#...#.###.###.###.###.###...#.###.###")
all_digits.append("#.#...#.#.....#...#...#.#.#...#.#.#...#")
all_digits.append("###...#.###.###...#.###.###...#.###.###")

each_digit = [[0] * 5 for _ in range(10)]
for i in range(5):
    for j in range(10):
        each_digit[j][i] = all_digits[i][4*j:4*j+3]
for i in range(10):
    each_digit[i] = "".join(each_digit[i])

# Get and Transform Inputs
N = int(input())
in_all_digits = []
for i in range(5):
    in_all_digits.append(input())

in_each_digit = [[0] * 5 for _ in range(N)]
for i in range(5):
    for j in range(N):
        in_each_digit[j][i] = in_all_digits[i][4*j:4*j+3]
for i in range(N):
    in_each_digit[i] = "".join(in_each_digit[i])
    
# Main Process
all_possible_numbers = [[] for _ in range(N)]
for i, in_digit in enumerate(in_each_digit):
    for d, digit in enumerate(each_digit):
        for c in range(15):
            if (digit[c] == ".") and (in_digit[c] == "#"):
                break
        else:
            all_possible_numbers[i].append(d)

nothing_possible = False
for possible_numbers in all_possible_numbers:
    if not possible_numbers:
        nothing_possible = True
        break
if nothing_possible:
    print(-1)
else:
    total = 0
    cnt = 1
    for possible_numbers in all_possible_numbers:
        new_cnt = len(possible_numbers)
        # sum: handle the total until now, and then new total
        total *= (10 * new_cnt)
        total += (sum(possible_numbers) * cnt)
        # count: multiplication(number of cases)
        cnt *= new_cnt
    print(total / cnt)
