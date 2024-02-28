# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return root

        queue, ans = deque([root]), []

        while len(queue)>0:
            level=[]

            for i in range(len(queue)):
                curr=queue.popleft()
                level.append(curr.val)
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            
            if len(ans) % 2 != 0:
                ans.append(level[::-1])
            else:
                ans.append(level)

        return ans

        