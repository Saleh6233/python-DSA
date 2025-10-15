from typing import Optional, List


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.leftchild = None
        self.rightchild = None


newBt = TreeNode("Drinks")
leftchild = TreeNode("Hot")
rightchild = TreeNode("Cold")

newBt.leftchild = leftchild
newBt.rightchild = rightchild


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


preOrderTraversal(newBt)
