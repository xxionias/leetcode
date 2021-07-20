
class Solution:
    def threeSum(self, nums, target):
        def twoSum(i, targetSum, res):
            l, r = i + 1, len(nums) - 1
            if l >= r or 2 * nums[l] > targetSum or 2 * nums[r] < targetSum:
                return
            while l < r:
                if nums[l] + nums[r] == targetSum:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif nums[l] + nums[r] < targetSum:
                    l += 1
                else:
                    r -= 1

        nums.sort()
        res = []
        for i in range(len(nums)):
            if 3 * nums[i] > target:
                break
            if i == 0 or nums[i] != nums[i - 1]:
                twoSum(i, target-nums[i], res)
        return res

sol = Solution()
print(sol.threeSum([-1, 0, 1, 1, 1, 4, 5, 6, 7, 8], 10))
