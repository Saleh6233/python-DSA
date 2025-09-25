"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

"""
from typing import Optional, List


class ListNode:
    """Simple singly-linked list node."""

    def __init__(self, x: int):
        self.val = x
        self.next: Optional["ListNode"] = None

    def __repr__(self) -> str:
        # helpful representation for debugging (does not try to print cycles)
        return f"ListNode({self.val})"


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Detect whether a singly linked list has a cycle.

        Uses Floyd's Tortoise and Hare algorithm (two pointers).
        - slow moves 1 step at a time
        - fast moves 2 steps at a time
        If there's a cycle, they will eventually meet.

        Time complexity: O(n)
        Space complexity: O(1)
        """
        # initialize both pointers at the head
        slow, fast = head, head

        # advance pointers until fast reaches the end (no cycle) or they meet (cycle)
        while fast is not None and fast.next is not None:
            # move fast by two steps
            fast = fast.next.next
            # move slow by one step
            slow = slow.next

            # if they meet, there is a cycle
            if slow == fast:
                return True

        # fast reached the end => no cycle
        return False


# ----------------- Helpers for building & testing -----------------
def build_linked_list(values: List[int], pos: int) -> Optional[ListNode]:
    """
    Build a linked list from `values`. If pos != -1, create a cycle by
    connecting the tail's next to the node at index `pos` (0-based).

    Args:
      values: list of integers for node values
      pos: index where tail should point to create a cycle, or -1 for no cycle

    Returns:
      head of the list (possibly None)
    """
    if not values:
        return None

    head = ListNode(values[0])
    tail = head
    nodes = [head]  # keep references so we can link tail to nodes[pos]
    for v in values[1:]:
        node = ListNode(v)
        tail.next = node
        tail = node
        nodes.append(node)

    # create cycle if requested and pos is valid
    if pos != -1:
        if 0 <= pos < len(nodes):
            tail.next = nodes[pos]
        else:
            raise IndexError("pos out of range when creating cycle")

    return head


def list_has_cycle_debug(head: Optional[ListNode]) -> bool:
    """
    Convenience wrapper for quick manual checks using Solution.hasCycle.
    """
    return Solution().hasCycle(head)


# ----------------- Example runs -----------------
if __name__ == "__main__":
    examples = [
        # (values, pos, expected) where pos is index to which tail links, -1 means no cycle
        ([3, 2, 0, -4], 1, True),   # tail connects to node index 1 -> cycle
        ([1, 2], 0, True),          # tail connects to node index 0 -> cycle
        ([1], -1, False),           # no cycle
    ]

    for i, (vals, pos, expected) in enumerate(examples, start=1):
        head = build_linked_list(vals, pos)
        result = list_has_cycle_debug(head)
        print(
            f"Case {i}: input={vals}, pos={pos} => hasCycle? {result} (expected: {expected})")
