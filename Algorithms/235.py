"""
235. Lowest Common Ancestor of a Binary Search Tree - Easy

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two
given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is
defined between two nodes p and q as the lowest node in T that has both p and q
as descendants (where we allow a node to be a descendant of itself).”



Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of
itself according to the LCA definition.

Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2


Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Algorithm

1. Start traversing the tree from the root node.
2. If both the nodes p and q are in the right subtree, then continue the search
with right subtree starting step 1.
3. If both the nodes p and q are in the left subtree, then continue the search
with left subtree starting step 1.
4. If both step 2 and step 3 are not true, this means we have found the node which
is common to node p's and q's subtrees. and hence we return this common node as the LCA.
"""
class RecursiveSolution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Value of current node or parent node.
        parent_val = root.val

        # Value of p
        p_val = p.val

        # Value of q
        q_val = q.val

        # If both p and q are greater than parent
        if p_val > parent_val and q_val > parent_val:
            return self.lowestCommonAncestor(root.right, p, q)
        # If both p and q are lesser than parent
        elif p_val < parent_val and q_val < parent_val:
            return self.lowestCommonAncestor(root.left, p, q)
        # We have found the split point, i.e. the LCA node.
        else:
            return root

class IterativeSolution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        p_val = p.val
        q_val = q.val

        node = root
        while node:
            parent_val = node.val

            # If both p and q are greater than parent
            if p_val > parent_val and q_val > parent_val:
                node = node.right
            # If both p and q are lesser than parent
            elif p_val < parent_val and q_val < parent_val:
                node = node.left
            # We have found the split point, i.e. the LCA node.
            else:
                return node
