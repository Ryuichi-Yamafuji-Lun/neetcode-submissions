# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right = []
        if not root: return right
        q = deque([root])
        while q:
            length = len(q)
            for i in range(length):
                current = q.popleft()
                if i == length - 1:
                    right.append(current.val)
                if current.left: q.append(current.left)
                if current.right: q.append(current.right)
        return right
        