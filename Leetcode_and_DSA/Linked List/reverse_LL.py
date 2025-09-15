"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Extra help: https://dipanjals-notebook.vercel.app/leetcode/linked-list/reverse-a-linked-list/

"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:

    # 'left' is head of the reversed portion (starts empty)
    left = None
    # 'right' is the current node we are processing (starts at original head)
    right = head

    while right:
        # Save the next node so we don't lose the remainder of the list
        catch_link = right.next

        # Reverse the current pointer: point current node to the reversed list
        right.next = left
        # Move 'left' pointer forward — now includes the node we just reversed
        left = right

        # Also move right pointer
        right = catch_link

     # 'left' is the new head of the reversed list
    return left


def build_linked_list(values: list[int]) -> Optional[ListNode]:
    """Create a linked list from a Python list and return its head (or None)."""
    if not values:
        return None
    head = ListNode(values[0])
    tail = head
    for v in values[1:]:
        tail.next = ListNode(v)
        tail = tail.next
    return head


def list_from_node(head: Optional[ListNode]) -> list[int]:
    """Convert a linked list starting at head into a Python list of values."""
    out: list[int] = []
    cur = head
    while cur:
        out.append(cur.val)
        cur = cur.next
    return out


if __name__ == "__main__":
    # Example 1: [1,2,3,4,5] -> [5,4,3,2,1]
    head1 = build_linked_list([1, 2, 3, 4, 5])
    print("Input :", list_from_node(head1))
    rev1 = reverseList(head1)
    print("Output:", list_from_node(rev1))
    print()

    # Example 2: [1,2] -> [2,1]
    head2 = build_linked_list([1, 2])
    print("Input :", list_from_node(head2))
    rev2 = reverseList(head2)
    print("Output:", list_from_node(rev2))
    print()

    # Example 3: [] -> []
    head3 = build_linked_list([])
    print("Input :", list_from_node(head3))
    rev3 = reverseList(head3)
    print("Output:", list_from_node(rev3))
