# Given the root of an n-ary tree, return the preorder traversal of its nodes' values.
# Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value .

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans=[]
        def preO(root):
            if root==None:
                return
            ans.append(root.val)
            for i in root.children:
                preO(i)
        preO(root)  
        return ans           
