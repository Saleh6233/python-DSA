"""
preorder_traversal.py

Recursive preorder traversal (LeetCode style) with comments and complexity notes.

Time complexity: O(n) — each node is visited exactly once.
Space complexity: O(h) call stack + O(n) for output list in total. Here h is the tree height;
                worst-case (skewed tree) h = n so recursion stack is O(n). The result list
                also stores n values, so overall auxiliary space is O(n), while recursion
                stack is O(h).
"""

from typing import Optional, List


class TreeNode:
    """Definition for a binary tree node (LeetCode-style)."""

    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """Return preorder traversal (root -> left -> right) of the tree as a list of values.

        This implementation uses recursion and accumulates results in `res`.
        """

        # List to hold traversal result
        res: List[int] = []

        def preOrderTraversal(rootNode: Optional[TreeNode]) -> None:
            """Helper recursive function.

            Visits node, then recurses on left and right children.
            """
            # Base case: reached the end of a branch
            if not rootNode:
                return

            # Visit the current node (append its value)

            res.append(rootNode.val)

            # Recurse to left subtree
            preOrderTraversal(rootNode.left)

            # Recurse to right subtree
            preOrderTraversal(rootNode.right)

        # Kick off recursion
        preOrderTraversal(root)
        return res


if __name__ == "__main__":
    # Small test that matches the problem example: root = [1, null, 2, 3]
    # Construct tree: 1 -> right -> 2, and 2 -> left -> 3
    root = TreeNode(1, None, TreeNode(2, TreeNode(3), None))

    solution = Solution()
    output = solution.preorderTraversal(root)
    print("Preorder traversal result:", output)  # Expected: [1, 2, 3]
