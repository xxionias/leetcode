"""
549. Binary Tree Longest Consecutive Sequence II - Medium

Given the root of a binary tree, return the length of the longest consecutive path
in the tree.

A consecutive path is a path where the values of the consecutive nodes in the path
differ by one. This path can be either increasing or decreasing.

For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is
not valid.
On the other hand, the path can be in the child-Parent-child order, where not necessarily
be parent-child order.



Example 1:

Input: root = [1,2,3]
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].

Example 2:

Input: root = [2,1,3]
Output: 3
Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].


Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-3 * 104 <= Node.val <= 3 * 104
"""
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        def longest_path(root):
            nonlocal maxVal

            if not root:
                return [0, 0]

            inr = dcr = 1
            if root.left:
                left = longest_path(root.left)
                if root.val == root.left.val + 1:
                    dcr = left[1] + 1
                elif root.val == root.left.val - 1:
                    inr = left[0] + 1

            if root.right:
                right = longest_path(root.right)
                if root.val == root.right.val + 1:
                    dcr = max(dcr, right[1] + 1)
                elif root.val == root.right.val - 1:
                    inr = max(inr, right[0] + 1)

            maxVal = max(maxVal, dcr + inr - 1)
            return [inr, dcr]

        maxVal = 0
        longest_path(root)
        return maxVal
