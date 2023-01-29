# Given an n-ary tree, return the level order traversal of its nodes' values.
# Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value.

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans=defaultdict(list)
        def levO(root,lev):
            if root==None:
                return
            ans[lev].append(root.val)
            for i in root.children:
                levO(i,lev+1)
        levO(root,0)  
        return [ls for k,ls in sorted(ans.items())]