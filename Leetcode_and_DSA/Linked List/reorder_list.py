from typing import Optional


class ListNode:
    """Singly-linked list node (LeetCode-style)."""

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"{self.val}"


class Solution:
    def getNodeBeforeMid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Return the node at the middle of the list (the node before the second half).
        For list lengths:
          - odd: returns exact middle (e.g. length 5 -> index 2)
          - even: returns the earlier middle so first half is longer (e.g. length 4 -> index 2)
        This allows splitting as:
          mid = getNodeBeforeMid(head)
          second = mid.next
          mid.next = None
        """
        if head is None or head.next is None:
            return head

        slow = head
        fast = head
        # move slow by 1 and fast by 2 until fast can't move
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverse a linked list and return the new head.
        """
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Reorder list to L0→Ln→L1→Ln-1→L2→...
        Modifies the list in-place and returns None.
        """
        if not head or not head.next or not head.next.next:
            return

        # use helper to find the node at the middle (before second half)
        # mid is the last node of first half
        mid = self.getNodeBeforeMid(head)
        second = mid.next
        mid.next = None                     # cut first half

        # reverse second half and merge
        second = self.reverse(second)

        first = head
        p1 = first
        p2 = second
        while p2:
            p1_next = p1.next
            p2_next = p2.next

            p1.next = p2
            p2.next = p1_next

            p1 = p1_next
            p2 = p2_next


def build_linked_list(values: list[int]) -> Optional[ListNode]:
    """Create linked list from Python list and return head (or None)."""
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
    out: list[int] = []
    cur = head
    while cur:
        out.append(cur.val)
        cur = cur.next
    return out


if __name__ == "__main__":
    sol = Solution()

    tests = [
        [1, 2, 3, 4, 5],   # odd length -> [1,5,2,4,3]
        [1, 2, 3, 4],      # even length -> [1,4,2,3]
        [1, 2],            # -> [1,2]
        [1],               # -> [1]
        [],                # -> []
    ]

    for vals in tests:
        head = build_linked_list(vals)
        print("Input: ", vals)
        sol.reorderList(head)
        print("Output:", list_from_node(head))
        print()
