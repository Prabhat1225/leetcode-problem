# Given the root of a binary tree, return all duplicate subtrees.
# For each kind of duplicate subtrees, you only need to return the root node of any one of them.
# Two trees are duplicate if they have the same structure with the same node values.
# Input: root = [1,2,3,4,null,2,4,null,null,4]
# Output: [[2,4],[4]]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        ans=[]
        map1={}
        def dfs(node,s):
            if node is None:
                return "#"
            s+=",".join([str(node.val),dfs(node.left,s),dfs(node.right,s)])    

            if s in map1:
                map1[s]+=1

                if map1[s]==2:
                    ans.append(node)
            else:
                map1[s]=1
            return s
        dfs(root," ")
        return ans                