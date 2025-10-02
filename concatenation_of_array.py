# Question
'''
Concatenation of Array

You are given an integer array nums of length n. Create an array ans of length 
2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.

Example 1:

Input: nums = [1,4,1,2]

Output: [1,4,1,2,1,4,1,2]

'''

# Solution

def ConcatenationOfArray(nums):
        n = len(nums)
        ans = [0] * ( 2* n)
        for i in range(n):
            ans[i] = nums[i]
            ans[i+n] = nums[i]
        return ans
