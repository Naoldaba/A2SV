# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        ans=0
        queue=deque([(root, 0)])

        while queue:
            n=len(queue)
            ans=max(ans, queue[-1][1]-queue[0][1]+1)

            for _ in range(n):
                curr, pos= queue.popleft()
                if curr.left:
                    queue.append((curr.left, 2*pos))
                if curr.right:
                    queue.append((curr.right, 2*pos + 1))

        return ans
        