# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr=[]

        def inorder(root):
            if root:
                inorder(root.left)
                arr.append(root.val)
                inorder(root.right)
        inorder(root)

        def balance(arr):
            if not arr:
                return 

            mid = len(arr)//2
            root=TreeNode(arr[mid])
            root.left=balance(arr[:mid])
            root.right=balance(arr[mid+1:])

            return root

        return balance(arr)
        

        
        