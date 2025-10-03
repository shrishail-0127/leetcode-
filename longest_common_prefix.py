'''
You are given an array of strings strs. Return the longest common prefix of all the strings.

If there is no longest common prefix, return an empty string "".

Example 1:

Input: strs = ["bat","bag","bank","band"]

Output: "ba"

'''


def longestCommonPrefix(strs):
        
    prefix = strs[0]

    for i in range(1, len(strs)):

        j = 0
        while j < min(len(prefix), len(strs[i])):
            if prefix[j] != strs[i][j]:
                break
            j += 1
        prefix = prefix[:j]

    return prefix