"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Remove the nth node from the end of the list and return the head.

    Args:
      head: head of the singly linked list (or None)
      n: 1-based position from the end (n == 1 means remove last node)

    Returns:
      Head of modified list (or None if list becomes empty).

    Time complexity: O(L) where L is the list length.
    Space complexity: O(1).
    """
    # Edge cases: empty list -> nothing to remove
    if head is None:
        return None

    # Dummy node simplifies deletion when the head must be removed.
    dummy = ListNode(-1, next=head)
    left = dummy         # left will end up just before the node to delete
    right = head         # right starts at head

    # Move right n steps ahead. After this:
    # - if n == length, right becomes None (so we will remove head)
    # - if n < length, right points n nodes ahead
    # - if n > length, this function treats it as invalid and returns original head
    steps = n
    while steps > 0 and right is not None:
        right = right.next
        steps -= 1

    if steps > 0:
        # n was larger than the list length; do nothing (safer than crashing).
        # You could raise an error instead if you prefer strict behavior.
        return head

    # Move left and right together until right reaches the end.
    # At that point, left.next is the node to remove.
    while right is not None:
        left = left.next
        right = right.next

    # Safety: ensure there is a node to remove
    if left.next is not None:
        left.next = left.next.next

    # Return the possibly-updated head
    return dummy.next


# ----------------- helpers & examples -----------------
def build_linked_list(values: list[int]) -> Optional[ListNode]:
    """Create a linked list from a Python list and return its head."""
    if not values:
        return None
    head = ListNode(values[0])
    tail = head
    for v in values[1:]:
        tail.next = ListNode(v)
        tail = tail.next
    return head


def list_from_node(head: Optional[ListNode]) -> list[int]:
    """Convert linked list starting at head into Python list of values."""
    out = []
    cur = head
    while cur:
        out.append(cur.val)
        cur = cur.next
    return out


if __name__ == "__main__":
    # Example 1
    head1 = build_linked_list([1, 2, 3, 4, 5])
    print("Input: ", list_from_node(head1), " n=2")
    head1 = removeNthFromEnd(head1, 2)
    print("Output:", list_from_node(head1))  # -> [1,2,3,5]
    print()

    # Example 2
    head2 = build_linked_list([1])
    print("Input: ", list_from_node(head2), " n=1")
    head2 = removeNthFromEnd(head2, 1)
    print("Output:", list_from_node(head2))  # -> []
    print()

    # Example 3
    head3 = build_linked_list([1, 2])
    print("Input: ", list_from_node(head3), " n=1")
    head3 = removeNthFromEnd(head3, 1)
    print("Output:", list_from_node(head3))  # -> [1]
    print()

    # Extra: n == length -> remove head
    head4 = build_linked_list([10, 20, 30])
    print("Input: ", list_from_node(head4), " n=3")
    head4 = removeNthFromEnd(head4, 3)
    print("Output:", list_from_node(head4))  # -> [20,30]
    print()

    # Extra: n > length -> no-op (safe behavior)
    head5 = build_linked_list([1, 2, 3])
    print("Input: ", list_from_node(head5), " n=5 (invalid)")
    head5 = removeNthFromEnd(head5, 5)
    print("Output:", list_from_node(head5))  # -> [1,2,3]
