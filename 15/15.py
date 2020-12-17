from typing import List

targets = (2020, 30000000)
use_test_cases = False

inputs = [([0,3,6], (436, 175594)),
          ([1,3,2], (1, 2578)),
          ([2,1,3], (10, 3544142)),
          ([1,2,3], (27, 261214)),
          ([2,3,1], (78, 6895259)),
          ([3,2,1], (438, 18)),
          ([3,1,2], (1836, 362)),
          ([9,19,1,6,0,5,4], (None, None))]

if not use_test_cases:
    inputs = inputs[-1:]


def find_target_number(nums: List[int], target: int) -> int:
    last_used = {}
    for i in range(len(nums) - 1):
        last_used[nums[i]] = i

    prev_num = nums[-1]
    for i in range(len(nums) - 1, target - 1):
        if prev_num in last_used:
            next_num = i - last_used[prev_num]
        else:
            next_num = 0
        
        last_used[prev_num] = i
        prev_num = next_num

    return prev_num


for i in range(2):
    for (nums, expected) in inputs:
        num = find_target_number(nums, targets[i])
        print(f"Input: {nums} -> {targets[i]}th number spoken is {num}", 
              f"(expected: {expected[i]})", flush=True)