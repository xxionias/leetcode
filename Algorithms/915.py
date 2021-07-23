"""
915. Partition Array into Disjoint Intervals - Medium

Given an array nums, partition it into two (contiguous) subarrays left and right so that:

- Every element in left is less than or equal to every element in right.
- left and right are non-empty.
- left has the smallest possible size.
Return the length of left after such a partitioning.  It is guaranteed that such
a partitioning exists.



Example 1:

Input: nums = [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]

Example 2:

Input: nums = [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]


Note:

2 <= nums.length <= 30000
0 <= nums[i] <= 106
It is guaranteed there is at least one way to partition nums as described.
"""
class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        N = len(A)
        maxleft = [0] * N
        minright = [0] * N

        m = A[0]
        for i in range(N):
            m = max(m, A[i])
            maxleft[i] = m

        m = A[-1]
        for i in reversed(range(N)):
            m = min(m, A[i])
            minright[i] = m

        for i in range(1, N):
            if maxleft[i - 1] <= minright[i]:
                return i
        
