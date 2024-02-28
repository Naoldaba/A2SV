# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def dfs(root,path, diff):
            
            path.append(root.val)
            
            if root.left:
                diff= dfs(root.left, path, diff)
            if root.right:
                diff= dfs(root.right, path, diff)
            if not root.left and not root.right:
                diff = max(diff, max(path)-min(path))

            path.pop()
            return diff

        return dfs(root, [], 0)





        