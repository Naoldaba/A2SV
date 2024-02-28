# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def sumLeaf(root, path, Sum):
            path.append(root.val)
            if root.left:
                Sum = sumLeaf(root.left, path, Sum)
            if root.right:
                Sum = sumLeaf(root.right, path, Sum)
            if not root.left and not root.right:
                Sum+=int(''.join(map(str, path)))
            path.pop()
            return Sum
        return sumLeaf(root, [0], 0)

            
        