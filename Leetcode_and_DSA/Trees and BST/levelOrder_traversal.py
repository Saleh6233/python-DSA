from typing import Optional, List
from collections import deque

# LeetCode-style TreeNode (uses .val, .left, .right)


class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Return level-order traversal as a list of levels: [[level0_vals], [level1_vals], ...]
        """
        if not root:
            return []

        result: List[List[int]] = []
        q = deque([root])

        while q:
            level_size = len(q)
            level_vals: List[int] = []

            # process exactly level_size nodes (current level)
            for _ in range(level_size):
                node = q.popleft()
                level_vals.append(node.val)

                # enqueue children for next level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(level_vals)

        return result


# Helper: build a binary tree from a LeetCode-style list (None for null)
def build_tree_from_list(values: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Build binary tree from list like [3,9,20,None,None,15,7].
    Returns the root TreeNode or None.
    """
    if not values:
        return None

    it = iter(values)
    root_val = next(it)
    if root_val is None:
        return None

    root = TreeNode(root_val)
    q = deque([root])

    for val in it:
        parent = q[0]  # peek parent (will pop when both children processed)
        # left child
        if parent.left is None:
            if val is not None:
                parent.left = TreeNode(val)
                q.append(parent.left)
            # move to right child for this parent next iteration
            continue
        # right child
        if parent.right is None:
            if val is not None:
                parent.right = TreeNode(val)
                q.append(parent.right)
            # finished both children for this parent -> pop it
            q.popleft()

    # Edge-case: if loop finished but left was set and right not processed,
    # parent may still be in queue but that's fine.
    return root


# ----------------- Small tests using the examples -----------------
if __name__ == "__main__":
    sol = Solution()

    # Example 1: root = [3,9,20,null,null,15,7]
    vals1 = [3, 9, 20, None, None, 15, 7]
    root1 = build_tree_from_list(vals1)
    # Expected: [[3], [9, 20], [15, 7]]
    print("Example 1 output:", sol.levelOrder(root1))

    # Example 2: root = [1]
    vals2 = [1]
    root2 = build_tree_from_list(vals2)
    print("Example 2 output:", sol.levelOrder(root2))  # Expected: [[1]]

    # Example 3: root = []
    vals3: List[Optional[int]] = []
    root3 = build_tree_from_list(vals3)
    print("Example 3 output:", sol.levelOrder(root3))  # Expected: []


# TreeNode class represents
# a node in a binary tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root):
        # Create a list to store levels
        ans = []
        if not root:
            # If the tree is empty,
            # return an empty list
            return ans

        # Create a queue to store nodes
        # for level-order traversal
        q = deque()
        # Enqueue the root node
        q.append(root)

        while q:
            # Get the size of the current level
            size = len(q)
            # Create a list to store
            # nodes at the current level
            level = []

            for i in range(size):
                # Get the front node in the queue
                node = q.popleft()
                # Store the node value
                # in the current level list
                level.append(node.val)

                # Enqueue the child nodes if they exist
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # Store the current level
            # in the answer list
            ans.append(level)
        # Return the level-order
        # traversal of the tree
        return ans

# Function to print
# the elements of a list


def printList(lst):
    # Iterate through the
    # list and print each element
    for num in lst:
        print(num, end=" ")
    print()


# Main function
if __name__ == "__main__":
    # Creating a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # Create an instance
    # of the Solution class
    solution = Solution()
    # Perform level-order traversal
    result = solution.levelOrder(root)

    print("Level Order Traversal of Tree:")

    # Printing the level order traversal result
    for level in result:
        printList(level)
