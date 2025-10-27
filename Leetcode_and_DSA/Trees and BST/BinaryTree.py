from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.leftchild = None
        self.rightchild = None


def preOrderTraversal(rootNode: Optional['TreeNode']) -> None:
    if not rootNode:
        return

    print(rootNode.data)

    preOrderTraversal(rootNode.leftchild)
    preOrderTraversal(rootNode.rightchild)


def inOrderTraversal(rootNode: Optional['TreeNode']) -> None:
    if not rootNode:
        return

    inOrderTraversal(rootNode.leftchild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightchild)


def postOrderTraversal(rootNode: Optional['TreeNode']) -> None:
    if not rootNode:
        return

    postOrderTraversal(rootNode.leftchild)
    postOrderTraversal(rootNode.rightchild)
    print(rootNode.data)


def levelOrderTraversal(rootNode: Optional['TreeNode']) -> None:
    if not rootNode:
        return
    else:
        queue = deque()
        queue.append(rootNode)

        while queue:
            node = queue.popleft()
            print(node.data)

            if node.leftchild:
                queue.append(node.leftchild)

            if node.rightchild:
                queue.append(node.rightchild)


def searchBT(rootNode: Optional['TreeNode'], nodeValue) -> bool:
    if not rootNode:
        return False
    else:
        queue = deque()
        queue.append(rootNode)

        while queue:
            node = queue.popleft()

            if node.data == nodeValue:
                return True

            if node.leftchild:
                queue.append(node.leftchild)

            if node.rightchild:
                queue.append(node.rightchild)

        return False


def insertNodeBT(rootNode: Optional['TreeNode'], newNode: Optional['TreeNode']) -> str:
    if not rootNode:
        rootNode = newNode
        return "Successfully inserted in root"
    else:
        queue = deque()
        queue.append(rootNode)

        while queue:
            node = queue.popleft()

            if node.leftchild:
                queue.append(node.leftchild)
            else:
                node.leftchild = newNode
                return "Successfully inserted in left"

            if node.rightchild:
                queue.append(node.rightchild)
            else:
                node.rightchild = newNode
                return "Successfully inserted in right"


def deleteDeepest(rootNode: TreeNode, d_node: TreeNode) -> None:
    """
    Remove the deepest node (d_node) from the tree rooted at rootNode.
    We find the parent of d_node and set the appropriate child to None.
    """
    queue = deque([rootNode])

    while queue:
        node = queue.popleft()
        # If this node's leftchild is the deepest node, remove it
        if node.leftchild:
            if node.leftchild is d_node:
                node.leftchild = None
                return
            else:
                queue.append(node.leftchild)

        # If this node's rightchild is the deepest node, remove it
        if node.rightchild:
            if node.rightchild is d_node:
                node.rightchild = None
                return
            else:
                queue.append(node.rightchild)


def deleteNodeBT(rootNode: Optional['TreeNode'], nodeValue) -> Optional['TreeNode']:
    """
    Delete the node whose .data == nodeValue from the binary tree (not BST).
    Returns the (possibly updated) root node (None if tree becomes empty).
    """

    # Empty tree
    if not rootNode:
        return None

    # If tree has only a single node
    if (rootNode.leftchild is None) and (rootNode.rightchild is None):
        if rootNode.data == nodeValue:
            # Deleting the only node -> tree becomes empty
            return None
        else:
            # target not found
            return rootNode

    key_node = None        # node to delete (by data)
    last_node = None       # deepest/rightmost node
    queue = deque([rootNode])

    # BFS to find key_node and also find last_node (deepest node)
    while queue:
        last_node = queue.popleft()

        if last_node.data == nodeValue:
            key_node = last_node

        if last_node.leftchild:
            queue.append(last_node.leftchild)
        if last_node.rightchild:
            queue.append(last_node.rightchild)

    # If we found the node to delete, replace its data with deepest node's data
    if key_node:
        key_node.data = last_node.data
        # remove the deepest node from the tree
        deleteDeepest(rootNode, last_node)
    # if key_node is None -> nodeValue not found; do nothing

    return rootNode


def deleteBT(rootnode) -> str:
    rootnode.data = None
    rootnode.leftchild = None
    rootnode.rightchild = None

    return "Successfully deleted tree"


if __name__ == "__main__":
    # Build a small tree:
    #        Drinks
    #       /      \
    #     Hot      Cold
    #    /   \       \
    #  Tea  Coffee   Soda
    root = TreeNode("Drinks")
    root.leftchild = TreeNode("Hot")
    root.rightchild = TreeNode("Cold")
    root.leftchild.leftchild = TreeNode("Tea")
    root.leftchild.rightchild = TreeNode("Coffee")
    root.rightchild.rightchild = TreeNode("Soda")

    # Expected print order:
    # Drinks
    # Hot
    # Cold
    # Tea
    # Coffee
    # Soda
    levelOrderTraversal(root)

    newNode = TreeNode("Cola")

    print(searchBT(root, "Soya"))

    print(insertNodeBT(root, newNode))
    levelOrderTraversal(root)
    # Build a small tree:
    #            Drinks
    #           /      \
    #          /        \
    #       Hot         Cold
    #      /   \       /   \
    #    Tea  Coffee Cola Soda
