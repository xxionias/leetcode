"""
16. 3Sum Closest - Medium

Given an array nums of n integers and an integer target, find three integers in
nums such that the sum is closest to target. Return the sum of the three integers.
You may assume that each input would have exactly one solution.



Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


Constraints:

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
"""
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float("inf")
        nums.sort()
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if abs(target - threeSum) < abs(diff):
                    diff = target - threeSum
                if threeSum < target:
                    l += 1
                else:
                    r -= 1
            if diff == 0:
                break
        return target - diff
