# Definition for a binary tree node.

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res: List[int] = []

        def inOrderTraversal(rootNode: Optional["TreeNode"]) -> None:
            if not rootNode:
                return

            inOrderTraversal(rootNode.left)
            res.append(rootNode.val)
            inOrderTraversal(rootNode.right)

        inOrderTraversal(root)

        return res
