class Solution:
    def fourSum(self, nums, target):
        def nSum(i, N, targetSum, result, results):
            if N < 2 or i >= len(nums) - 1 or nums[i] * N > targetSum or nums[-1] * N < targetSum:
                return
            if N == 2:
                l, r = i, len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] == targetSum:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif nums[l] + nums[r] < targetSum:
                        l += 1
                    else:
                        r -= 1
            else:
                for j in range(i, len(nums)):
                    if j == i or nums[j] != nums[j - 1]:
                        nSum(j + 1, N - 1, targetSum - nums[j], result + [nums[j]], results)

        nums.sort()
        results = []
        nSum(0, 4, target, [], results)
        return results

sol = Solution()
print(sol.fourSum([-1, 0, -5, 1, 2, 3, 4, 5, 6, 7, 8, 9], 7))
