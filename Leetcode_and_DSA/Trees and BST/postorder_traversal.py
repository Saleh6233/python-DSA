# Definition for a binary tree node.

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res: List[int] = []

        def postOrder(rootNode: Optional["TreeNode"]) -> None:
            if not rootNode:
                return

            postOrder(rootNode.left)
            postOrder(rootNode.right)
            res.append(rootNode.val)

        postOrder(root)

        return res
