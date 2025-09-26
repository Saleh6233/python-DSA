"""
iven the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:


The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Custom Judge:

The inputs to the judge are given as follows (your program is not given these inputs):

intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.

 

Example 1:


Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
- Note that the intersected node's value is not 1 because the nodes with value 1 in A and B (2nd node in A and 3rd node in B) are different node references. In other words, they point to two different locations in memory, while the nodes with value 8 in A and B (3rd node in A and 4th node in B) point to the same location in memory.
Example 2:


Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'
Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
Example 3:


Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection
Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.

"""

from typing import Optional, Tuple, List


class ListNode:
    """Simple singly-linked list node."""

    def __init__(self, x: int):
        self.val = x
        self.next: Optional["ListNode"] = None

    def __repr__(self) -> str:
        return f"ListNode({self.val})"


class Solution:
    def getIntersectionNode(self, headA: Optional[ListNode], headB: Optional[ListNode]) -> Optional[ListNode]:
        """
        Return the node where two singly linked lists intersect, or None if they don't.
        Uses the two-pointer switching technique:
          - Advance two pointers pA and pB; when a pointer reaches the end, switch it to
            the head of the other list. If lists intersect, pointers meet at the intersection.
        Time: O(m + n), Space: O(1)
        """
        if headA is None or headB is None:
            return None

        pA, pB = headA, headB

        # Continue until pointers meet (either at intersection node or both None)
        while pA is not pB:
            # move to next or switch to other head when reaching the end
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA

        # either both None (no intersection) or the intersection node
        return pA


# ---------------- Helper: build two lists with optional intersection ----------------
def build_intersecting_lists(listA: List[int], listB: List[int], skipA: int, skipB: int
                             ) -> Tuple[Optional[ListNode], Optional[ListNode]]:
    """
    Build two linked lists from `listA` and `listB`. If skipA and skipB point inside
    their respective lists (0 <= skip < len(list)), this will create an intersection by
    making the node at index skipB in listB point to the node at index skipA in listA.
    This mirrors LeetCode's construction: the shared tail is the suffix of listA starting
    at skipA.

    Returns (headA, headB).
    """
    # Build nodes for list A
    nodesA: List[ListNode] = []
    headA = None
    tailA = None
    for v in listA:
        node = ListNode(v)
        nodesA.append(node)
        if headA is None:
            headA = node
            tailA = node
        else:
            tailA.next = node
            tailA = node

    # Build nodes for list B (only prefix for now)
    nodesB: List[ListNode] = []
    headB = None
    tailB = None
    for v in listB:
        node = ListNode(v)
        nodesB.append(node)
        if headB is None:
            headB = node
            tailB = node
        else:
            tailB.next = node
            tailB = node

    # Decide whether to create intersection:
    # We create an intersection only when both skip indices are valid.
    if 0 <= skipA < len(nodesA) and 0 <= skipB < len(nodesB):
        # Connect the node at index skipB in listB to node at index skipA in listA
        # The shared tail becomes nodesA[skipA:] (same objects).
        # To do that, link the node before skipB (if it exists) to nodesA[skipA].
        if skipB == 0:
            # headB should start at intersection node
            headB = nodesA[skipA]
        else:
            nodesB[skipB - 1].next = nodesA[skipA]
        # ensure tailB is updated (not strictly necessary here)
    # else: no intersection created; lists remain separate

    return headA, headB


# ---------------- Helpers for printing/testing ----------------
def print_list(head: Optional[ListNode], limit: int = 20) -> None:
    """
    Print node values up to `limit` nodes (prevents infinite loops if something is cyclic).
    """
    out = []
    cur = head
    steps = 0
    while cur and steps < limit:
        out.append(str(cur.val))
        cur = cur.next
        steps += 1
    if cur:
        out.append("...")
    print(" -> ".join(out) if out else "Empty")


def test_example(intersectVal: int, listA: List[int], listB: List[int], skipA: int, skipB: int) -> None:
    """
    Build lists according to the example parameters, run the solution and print result.
    Note: We create an intersection only if skip indices are valid (0 <= skip < len).
    """
    headA, headB = build_intersecting_lists(listA, listB, skipA, skipB)
    print("List A:", end=" ")
    print_list(headA)
    print("List B:", end=" ")
    print_list(headB)
    res = Solution().getIntersectionNode(headA, headB)
    if res:
        print(f"Intersected at node with value: {res.val}")
    else:
        print("No intersection")
    print("-" * 40)


# ---------------------- Example runs (from prompt) ----------------------
if __name__ == "__main__":
    # Example 1:
    # listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], intersection at index 2 of A and 3 of B
    test_example(intersectVal=8, listA=[4, 1, 8, 4, 5], listB=[
                 5, 6, 1, 8, 4, 5], skipA=2, skipB=3)

    # Example 2:
    test_example(intersectVal=2, listA=[1, 9, 1, 2, 4], listB=[
                 3, 2, 4], skipA=3, skipB=1)

    # Example 3 (no intersection):
    # skipA = 3 equals len(listA) so we won't create an intersection here
    test_example(intersectVal=0, listA=[2, 6, 4], listB=[
                 1, 5], skipA=3, skipB=2)
