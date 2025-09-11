"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

"""
from typing import Optional

# Definition for singly-linked list node (same shape as LeetCode's ListNode).


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next

            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        tail.next = list1 if list1 is not None else list2

        return dummy.next


def build_linked_list(values: list[int]) -> Optional[ListNode]:
    """Build a linked list from a Python list and return its head (or None)."""
    if not values:
        return None
    head = ListNode(values[0])
    tail = head
    for v in values[1:]:
        tail.next = ListNode(v)
        tail = tail.next
    return head


def linked_list_to_list(head: Optional[ListNode]) -> list[int]:
    """Convert a linked list to a Python list of values (for easy printing)."""
    out = []
    cur = head
    while cur:
        out.append(cur.val)
        cur = cur.next
    return out


if __name__ == "__main__":
    # Example 1
    l1 = build_linked_list([1, 2, 4])
    l2 = build_linked_list([1, 3, 4])

    merged = Solution().mergeTwoLists(l1, l2)
    print(linked_list_to_list(merged))  # -> [1, 1, 2, 3, 4, 4]

    # Example 2
    print(linked_list_to_list(Solution().mergeTwoLists(
        build_linked_list([]), build_linked_list([]))))  # -> []

    # Example 3
    print(linked_list_to_list(Solution().mergeTwoLists(
        build_linked_list([]), build_linked_list([0]))))  # -> [0]
