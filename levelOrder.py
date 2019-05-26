from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        traverse = []
        q = [root]
        while q:
            curLevelSize = len(q)
            curLevel = []
            for _ in range(curLevelSize):
                curNode = q.pop(0)
                curLevel.append(curNode.val)
                if curNode.left:
                    q.append(curNode.left)

                if curNode.right:
                    q.append(curNode.right)

            traverse.append(curLevel)

        return traverse


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

sol = Solution()
print(sol.levelOrder(root))
