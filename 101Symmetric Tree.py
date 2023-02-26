# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def Same(p,q):
            if not p and not q:
                return True
            if not p or not q or p.val!=q.val:
                return False
            return Same(p.left , q.right) and Same(p.right , q.left)
        return Same(root.left,root.right)                                