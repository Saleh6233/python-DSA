"""
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
Example 2:


Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
Example 3:


Input: head = [1], pos = -1
Output: no cycle
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
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Detect the node where a cycle begins in a singly linked list.
        Uses Floyd's algorithm with an explicit has_cycle boolean.

        Returns:
          - the node where the cycle starts, or
          - None if there is no cycle.

        Time: O(n)
        Space: O(1)
        """
        # Fast/slow pointers for cycle detection
        slow = head
        fast = head
        has_cycle = False  # explicit flag set when slow meets fast

        # 1) Detect if a cycle exists by advancing fast twice and slow once
        while fast is not None and fast.next is not None:
            slow = slow.next          # advance slow by 1
            fast = fast.next.next     # advance fast by 2
            if slow == fast:
                # meeting point found -> there is a cycle
                has_cycle = True
                break

        # 2) If no cycle detected, return None
        if not has_cycle:
            return None

        # 3) To find the entry point of the cycle:
        #    Move a pointer from the head and another from the meeting point,
        #    advancing both one step at a time. They meet at the cycle start.
        ptr = head
        while ptr != slow:
            ptr = ptr.next
            slow = slow.next

        return ptr


# ---------------- Helpers for building/testing ----------------
def build_linked_list(values: List[int], pos: int) -> Optional[ListNode]:
    """
    Build a linked list from `values`. If pos != -1, create a cycle by
    connecting the tail's next to the node at index `pos` (0-based).
    Returns the head of the list.
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

    if pos != -1:
        if 0 <= pos < len(nodes):
            tail.next = nodes[pos]  # create cycle
        else:
            raise IndexError("pos out of range when creating cycle")

    return head


def show_detect_cycle(values: List[int], pos: int) -> None:
    """
    Build the list with given values and pos, run detectCycle, and print result.
    """
    head = build_linked_list(values, pos)
    start = Solution().detectCycle(head)
    if start:
        print(
            f"List {values} with pos={pos} -> cycle starts at node with val = {start.val}")
    else:
        print(f"List {values} with pos={pos} -> no cycle detected")


# ---------------- Example runs ----------------
if __name__ == "__main__":
    # Examples from the prompt
    show_detect_cycle([3, 2, 0, -4], 1)  # expected start val = 2
    show_detect_cycle([1, 2], 0)         # expected start val = 1
    show_detect_cycle([1], -1)           # expected no cycle (None)

    # Extra quick checks
    show_detect_cycle([], -1)            # empty list -> no cycle
    show_detect_cycle([1, 2, 3, 4, 5], 2)  # cycle starting at value 3
