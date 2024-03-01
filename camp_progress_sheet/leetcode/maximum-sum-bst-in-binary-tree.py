# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:

        Max = 0
        def search(root):
            nonlocal Max
            if root is None:
                return 1, inf, -inf, 0      
            
            l, min_l, max_l, sum_l = search(root.left)
            r, min_r, max_r, sum_r = search(root.right)
            
            if l and r and max_l < root.val < min_r:
                cur = sum_l + sum_r + root.val
                
                Max = max(cur, Max)
                min_l = min(min_l, root.val)
                max_r = max(max_r, root.val)
                return 1, min_l, max_r, cur
            else:
                return 0, 0, 0, 0
                
        search(root)
        return Max