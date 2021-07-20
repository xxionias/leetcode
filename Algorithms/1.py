"""
Time Complexity: O(N)
Space Complexity: O(N)

Initiate a dictionary
Iterate through list
for each element, check if there is an element in the dictionary s.t. their sum equals the target
    if so, append the tuple to the result list
    if not, insert the element into the dictionary with its index
"""
class Solution:
    def twoSum(self, nums, target):
        diff_map = {}
        for i, e in enumerate(nums):
            if e in d:
                return [diff_map[e], i]
            diff_map[target - e] = i
        return []
