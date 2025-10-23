"""

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """
        Calculate the maximum depth of a binary tree using recursion.

        :param root: TreeNode - root of the binary tree
        :return: int - maximum depth of the tree
        """

        # Base case: if the tree is empty, its depth is 0
        if not root:
            return 0

        # Recursively find the depth of left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # The depth of the current node is 1 + the deeper subtree
        return 1 + max(left_depth, right_depth)


# Example usage
if __name__ == "__main__":
    # Construct the binary tree:
    #        3
    #       / \
    #      9  20
    #         / \
    #        15  7

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))

    # Create Solution instance and compute depth
    sol = Solution()
    print("Maximum Depth of Binary Tree:", sol.maxDepth(root))
