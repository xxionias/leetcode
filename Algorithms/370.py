"""
370. Range Addition - Medium

You are given an integer length and an array updates where updates[i] = [startIdx_i, endId_xi, inc_i].

You have an array arr of length length with all zeros, and you have some operation
to apply on arr. In the ith operation, you should increment all the elements arr[startIdx_i],
arr[startIdx_i + 1], ..., arr[endIdx_i] by inc_i.

Return arr after applying all the updates.



Example 1:

Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
Output: [-2,0,3,5,3]

Example 2:

Input: length = 10, updates = [[2,4,6],[5,6,8],[1,9,-4]]
Output: [0,-4,2,2,2,4,4,-4,-4,-4]


Constraints:

1 <= length <= 105
0 <= updates.length <= 104
0 <= startIdxi <= endIdxi < length
-1000 <= inci <= 1000
"""
class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        ans = [0] * length

        for start, end, val in updates:
            ans[start] += val
            if end + 1 < length:
                ans[end + 1] -= val

        for i in range(1, length):
            ans[i] += ans[i - 1]

        return ans
