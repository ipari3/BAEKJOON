import sys
from collections import Counter, defaultdict

# get inputs
N, *input_nums = map(int, sys.stdin.readlines())

# variables
nums_counter = Counter(input_nums)
max_num = max(nums_counter)
touch_per_num = defaultdict(int)

# main process
for num, cnt in nums_counter.items():
    touch_per_num[num] += cnt - 1
    for multiple in range(2*num, max_num+1, num):
        if multiple in nums_counter:
                touch_per_num[multiple] += cnt

for num in input_nums:
    print(touch_per_num[num])