""" You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list. The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x. For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively. Example 1: Input: head = [1,3,4,7,1,2,6] Output: [1,3,4,1,2,6] Explanation: The above figure represents the given linked list. The indices of the nodes are written below. Since n = 7, node 3 with value 7 is the middle node, which is marked in red. We return the new list after removing this node. Example 2: Input: head = [1,2,3,4] Output: [1,2,4] Explanation: The above figure represents the given linked list. For n = 4, node 2 with value 3 is the middle node, which is marked in red. Example 3: Input: head = [2,1] Output: [2] Explanation: The above figure represents the given linked list. For n = 2, node 1 with value 1 is the middle node, which is marked in red. Node 0 with value 2 is the only node remaining after removing node 1. """


from typing import Optional


class ListNode:

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def move_before_mid(head: Optional[ListNode]) -> Optional[ListNode]:

    # Safety checks: if list is empty or has only one node, return head itself.
    if head is None or head.next is None:
        return head

    # slow will trail and end up before the middle.
    # fast starts two steps ahead (so when fast reaches end, slow is before middle).
    slow = head
    fast = head.next.next

    # advance slow by 1 and fast by 2 while possible
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    # slow now points to node before the middle (for list length >= 2)
    return slow


def deleteMiddle(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Delete the middle node from the linked list and return the (possibly new) head.

    Middle is floor(n/2) using 0-based indexing. If list has 1 node, return None.

    Time complexity: O(n)
    Space complexity: O(1)
    """
    # empty list -> nothing to delete
    if head is None:
        return None

    # single-node list -> becomes empty after deletion
    if head.next is None:
        return None

    # find the node before middle and skip the middle node
    before_mid = move_before_mid(head)
    # before_mid.next is the middle node; skip it
    before_mid.next = before_mid.next.next

    # head remains the same (unless original list had one node, handled above)
    return head


# ---------- small helpers for testing ----------
def build_linked_list(values: list[int]) -> Optional[ListNode]:
    """Build a linked list from Python list and return head (or None)."""
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
    out = []
    cur = head
    while cur:
        out.append(cur.val)
        cur = cur.next
    return out


if __name__ == "__main__":
    # Example 1
    head1 = build_linked_list([1, 3, 4, 7, 1, 2, 6])
    print("Input: ", list_from_node(head1))
    head1 = deleteMiddle(head1)
    print("Output:", list_from_node(head1))  # -> [1,3,4,1,2,6]
    print()

    # Example 2
    head2 = build_linked_list([1, 2, 3, 4])
    print("Input: ", list_from_node(head2))
    head2 = deleteMiddle(head2)
    print("Output:", list_from_node(head2))  # -> [1,2,4]
    print()

    # Example 3
    head3 = build_linked_list([2, 1])
    print("Input: ", list_from_node(head3))
    head3 = deleteMiddle(head3)
    print("Output:", list_from_node(head3))  # -> [2]
    print()

    # Extra: single-node list
    head4 = build_linked_list([10])
    print("Input: ", list_from_node(head4))
    head4 = deleteMiddle(head4)
    print("Output:", list_from_node(head4))  # -> []
