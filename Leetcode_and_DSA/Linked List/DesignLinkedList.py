"""
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
 

Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3

"""

#!/usr/bin/env python3
"""
my_linked_list.py

Standalone script implementing a doubly-linked list with sentinel head/tail nodes.
Includes a small demo and assertions to verify basic behavior.
"""


from typing import Optional
class Node:
    def __init__(self, val: int, prev: 'Optional[Node]' = None, next: 'Optional[Node]' = None):
        self.val = val
        self.prev = prev
        self.next = next

    def __repr__(self):
        return f"Node({self.val})"


class MyLinkedList:
    def __init__(self):
        self.size = 0
        # Dummy head and tail sentinels
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def getNthNode(self, curr: 'Optional[Node]', index: int) -> 'Optional[Node]':
        """
        Move forward `index` steps from `curr`. Return the node reached or None.
        (Assumes index >= 0)
        """
        while curr is not None and index > 0:
            curr = curr.next
            index -= 1
        return curr

    def get(self, index: int) -> int:
        """Return the value of the index-th node in the linked list. If invalid, return -1."""
        if index < 0 or index >= self.size:
            return -1
        firstNode = self.head.next
        nthNode = self.getNthNode(firstNode, index)
        return nthNode.val if nthNode is not None else -1

    def insertNode(self, value: int, prevNode: Node, nextNode: Node) -> None:
        """Insert a new node with value between prevNode and nextNode."""
        newNode = Node(value, prev=prevNode, next=nextNode)
        prevNode.next = newNode
        nextNode.prev = newNode
        self.size += 1

    def addAtHead(self, val: int) -> None:
        self.insertNode(val, prevNode=self.head, nextNode=self.head.next)

    def addAtTail(self, val: int) -> None:
        self.insertNode(val, prevNode=self.tail.prev, nextNode=self.tail)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals the length, the node will be appended to the end.
        If index is greater than the length, nothing will happen.
        If index is negative, node is inserted at head (index 0).
        """
        if index < 0:
            index = 0
        if index > self.size:
            return
        # prevNode should be the node after moving `index` steps from head
        prevNode = self.getNthNode(self.head, index)
        # prevNode is guaranteed to exist (head exists and index <= size)
        self.insertNode(val, prevNode=prevNode, nextNode=prevNode.next)

    def deleteNode(self, nthNode: Node) -> None:
        """Unlink nthNode from the list."""
        prevNode = nthNode.prev
        nextNode = nthNode.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        self.size -= 1

    def deleteAtIndex(self, index: int) -> None:
        """Delete the index-th node in the linked list, if the index is valid."""
        if index < 0 or index >= self.size:
            return
        nthNode = self.getNthNode(self.head.next, index)
        if nthNode is not None:
            self.deleteNode(nthNode)

    def to_list(self) -> list:
        """Return the list of values (for easy printing/testing)."""
        vals = []
        node = self.head.next
        while node is not None and node is not self.tail:
            vals.append(node.val)
            node = node.next
        return vals

    def __repr__(self):
        return "MyLinkedList(" + " <-> ".join(map(str, self.to_list())) + ")"


def demo():
    """
    Demonstration of functionality.
    Uses the classic sequence:
    addAtHead(1), addAtTail(3), addAtIndex(1,2), get(1) -> 2,
    deleteAtIndex(1), get(1) -> 3
    """
    print("Demo: running basic operations...")
    obj = MyLinkedList()

    print("Initial:", obj)
    obj.addAtHead(1)
    print("After addAtHead(1):", obj)
    obj.addAtTail(3)
    print("After addAtTail(3):", obj)
    obj.addAtIndex(1, 2)   # linked list becomes 1->2->3
    print("After addAtIndex(1, 2):", obj)

    res1 = obj.get(1)      # returns 2
    print("get(1) ->", res1)
    assert res1 == 2, "Expected get(1) == 2"

    obj.deleteAtIndex(1)   # now the list is 1->3
    print("After deleteAtIndex(1):", obj)

    res2 = obj.get(1)      # returns 3
    print("get(1) ->", res2)
    assert res2 == 3, "Expected get(1) == 3"

    # Additional quick checks
    assert obj.to_list() == [
        1, 3], f"Expected final list [1, 3], got {obj.to_list()}"
    print("All demo checks passed!")


if __name__ == "__main__":
    demo()
