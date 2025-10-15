
# Single Number
'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:

Input: nums = [2,2,1]

Output: 1

Example 2:

Input: nums = [4,1,2,1,2]

Output: 4

Example 3:

Input: nums = [1]

Output: 1

'''

# Answers

def single_number(nums):
    seen = {}
    for i , num in enumerate(nums):
        if num in seen:
            seen[num] += 1
            continue
        seen[num] = 1
    for k,v in  seen.items():
        print(k,v)
        if v == 1:
            return k
        

def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result