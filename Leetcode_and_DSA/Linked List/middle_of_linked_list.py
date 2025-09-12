"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return None

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


def build_linked_list(values: list[int]) -> Optional[ListNode]:
    """Build a linked list from a Python list and return its head."""
    if not values:
        return None
    head = ListNode(values[0])
    tail = head
    for v in values[1:]:
        tail.next = ListNode(v)
        tail = tail.next
    return head


def list_from_node(head: Optional[ListNode]) -> list[int]:
    """Return a Python list of node values starting from head (useful to show the returned sublist)."""
    out = []
    cur = head
    while cur:
        out.append(cur.val)
        cur = cur.next
    return out


# ---------- Example usage ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1: [1,2,3,4,5] -> middle is 3 -> [3,4,5]
    head1 = build_linked_list([1, 2, 3, 4, 5])
    mid1 = sol.middleNode(head1)
    print("Input:", [1, 2, 3, 4, 5])
    print("Output:", list_from_node(mid1))  # -> [3, 4, 5]
    print()

    # Example 2: [1,2,3,4,5,6] -> middle second is 4 -> [4,5,6]
    head2 = build_linked_list([1, 2, 3, 4, 5, 6])
    mid2 = sol.middleNode(head2)
    print("Input:", [1, 2, 3, 4, 5, 6])
    print("Output:", list_from_node(mid2))  # -> [4, 5, 6]
    print()

    # Extra: empty list
    head3 = build_linked_list([])
    mid3 = sol.middleNode(head3)
    print("Input:", [])
    print("Output:", list_from_node(mid3))  # -> []
