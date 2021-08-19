# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def gatherVals(tree):
            arr = []
            while tree:
                arr.append(tree.val)
                if tree.left:
                    arr += gatherVals(tree.left)
                else:
                    arr += "null"
                if tree.right:
                    arr += gatherVals(tree.right)
                else:
                    arr += "null"
                return arr
        x = gatherVals(p)
        y = gatherVals(q)

        if x == y:
            return True
        else:
            return False
