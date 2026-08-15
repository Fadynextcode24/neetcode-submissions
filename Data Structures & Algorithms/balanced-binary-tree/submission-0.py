# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0
            lefty = dfs(root.left)
            if lefty == -1:
                return -1
            righty = dfs(root.right)
            if righty == -1:
                return -1
            if abs(lefty-righty) > 1:
                return -1
            return 1 + max(lefty,righty)
        return dfs(root)!=-1
        