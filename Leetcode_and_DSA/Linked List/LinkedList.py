class Node:
    """A single node in a singly linked list."""

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """Singly linked list with head, tail and length attributes."""

    def __init__(self, value):
        """
        Initialize the linked list with a single node containing `value`.
        head and tail both point to that node, length starts at 1.

        """
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def printLL(self):
        """
        Walk the list from head to tail and print each node's value.
        This does not modify the list.

        """

        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next

    def append(self, value):
        """
        Append a new node with `value` to the end of the list.
        Runs in O(1) time because we keep a reference to tail.
        Returns True on success.
        """
        new_node = Node(value)
        if self.length == 0:
          # empty list: head and tail both become the new node
            self.head = new_node
            self.tail = new_node
        else:
            # non-empty list: link current tail to new node, then update tail
            # `self.tail` is guaranteed to be a Node here (not None), so assigning
            # its `next` to the new_node links the list.
            self.tail.next = new_node  # type: ignore
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        """
        Remove and return the last node from the linked list.
        Returns the removed Node (not its value), or None if the list is empty.
        Time complexity: O(n) because we must traverse to the end to find the node before tail.
        """
        # If the list is empty, nothing to pop
        if self.length == 0:
            return None

        # `temp` will walk to the last node, `pre` will follow behind as the node before `temp`
        temp = self.head
        pre = self.head

        # Traverse until temp is the last node (temp.next is None)
        while temp.next:
            pre = temp      # keep `pre` one node behind `temp`
            temp = temp.next

        # At this point:
        # - `temp` is the node to remove (the current tail)
        # - `pre` is the node right before `temp` (becomes the new tail)
        self.tail = pre        # update tail to the previous node
        self.tail.next = None  # disconnect the old tail from the list
        self.length -= 1       # decrease length since we've removed a node

        # If the list became empty after removal, clear head and tail references
        if self.length == 0:
            self.head = None
            self.tail = None

        # Return the removed node
        return temp

    def prepend(self, value):
        """
        Insert a new node with `value` at the start (head) of the list.
        Runs in O(1) time because we only change a couple of pointers.
        Returns True on success.
        """
        new_node = Node(value)

        if self.length == 0:
            # empty list: head and tail both become the new node
            self.head = new_node
            self.tail = new_node
        else:
            # non-empty list: point new_node to current head, then update head
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True

    def pop_first(self):
        """
        Remove and return the first node of the linked list.

        Behaviour:
        - If the list is empty, return None.
        - Otherwise remove the head node, update head (and tail if list becomes empty),
            decrement length, and return the removed node.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        # empty list -> nothing to remove
        if self.length == 0:
            return None

        # save current head (node to remove)
        temp = self.head

        # advance head to the next node (this unlinks the first node from the list)
        self.head = self.head.next

        # detach removed node from list to avoid dangling references
        temp.next = None

        # decrement stored length
        self.length -= 1

        # if the list is now empty (we removed the only node), clear tail as well
        if self.length == 0:
            self.tail = None

        # return the removed node (caller can inspect .value/.val or re-link it)
        return temp

    def get(self, index: int):
        """
        Return the node at `index` (0-based).
        Returns None if index is out of bounds.

        Time complexity: O(n)
        Space complexity: O(1)
        """
        # quick bounds check (negative or past end)
        if index < 0 or index >= self.length:
            return None

        # start from the head and walk `index` steps
        temp = self.head
        for _ in range(index):
            temp = temp.next

        # temp now refers to the node at `index`; return its value
        return temp

    def set_value(self, index: int, value) -> bool:
        """
        Set the node at `index` to `value` using the get() helper.

        Returns True on success, False if index is out of bounds.

        Time: O(n) — dominated by get()
        Space: O(1)
        """
        node = self.get(index)   # reuses get to locate the node
        if node is None:
            return False
        node.value = value
        return True

    def insert(self, index: int, value) -> bool:
        """
        Insert a new node with `value` at position `index` (0-based).

        Returns:
        True if insertion succeeded, False if index is out of bounds.

        Time complexity: O(n) in the worst case (needs to walk to index-1).
        Space complexity: O(1)
        """
        # valid indexes for insert are 0..length (inclusive at end)
        if index < 0 or index > self.length:
            return False

        # insert at head
        if index == 0:
            return self.prepend(value)

        # insert at tail (append)
        if index == self.length:
            return self.append(value)

        # middle insertion:
        # create the new node to insert
        new_node = Node(value)

        # find node before insertion point (assumes get returns the Node)
        prev = self.get(index - 1)
        # safety: if get unexpectedly returned None, fail gracefully
        if prev is None:
            return False

        # splice the new node in
        new_node.next = prev.next
        prev.next = new_node

        # update length
        self.length += 1
        return True

    def remove(self, index):
        """
        Remove and return the node at `index` (0-based).
        Returns:
        - the removed node on success
        - None if index is out of bounds

        Time complexity: O(n)
        Space complexity: O(1)
        """
        # bounds check: valid indexes are 0 .. self.length-1
        if index < 0 or index >= self.length:
            return None

        # remove head
        if index == 0:
            return self.pop_first()

        # remove tail
        if index == self.length - 1:
            return self.pop()

        # find node before the one we want to remove
        prev = self.get(index - 1)  # assumes get returns the Node
        # safety check: if get unexpectedly returned None, abort
        if prev is None or prev.next is None:
            return None

        # unlink the node to remove
        temp = prev.next           # node to remove
        prev.next = temp.next      # bypass temp
        temp.next = None          # detach temp from list
        self.length -= 1          # decrement length

        return temp               # return removed node

    def reverse(self):
        """
        Reverse the linked list in-place.

        Behaviour:
        - After calling, head points to the original tail, and tail points to the original head.
        - Works correctly for empty and single-node lists (no-op).

        Time complexity: O(n)
        Space complexity: O(1)
        """
        # empty or single-node list -> nothing to do
        if self.head is None or self.head.next is None:
            return

        prev = None              # previous node (becomes new next)
        curr = self.head         # current node we are processing
        self.tail = self.head    # original head will become the new tail

        # iterate and reverse pointers
        while curr is not None:
            # save next node (so we don't lose the remainder)
            nxt = curr.next
            curr.next = prev     # reverse the pointer
            prev = curr          # advance prev to include curr
            curr = nxt           # move to next node in original list

        # prev is the new head (original tail)
        self.head = prev


if __name__ == "__main__":

    my_linked_list = LinkedList(4)
    my_linked_list.append(2)

    print('Head:', my_linked_list.head.value)
    print('Tail:', my_linked_list.tail.value)
    print('Length:', my_linked_list.length, '\n')

    print('Linked List:')
    my_linked_list.printLL()

    print('\n', 'Removing all values:')
    print(my_linked_list.pop())
    print(my_linked_list.pop())

    my_linked_list.prepend(3)
    print('Linked List:')
    my_linked_list.printLL()

    print("\n", 'Using Pop first')
    print(my_linked_list.pop_first())
    print(my_linked_list.pop_first())

    my_linked_list.append(12)
    my_linked_list.append(15)
    my_linked_list.append(34)
    my_linked_list.append(7)

    print('\nLinked List:')
    my_linked_list.printLL()

    print("\nGet value at index 2 is:")
    print(my_linked_list.get(2))

    print("\nChanging value at index 2 is:")
    my_linked_list.set_value(2, 3)

    print('\nLinked List:')
    my_linked_list.printLL()

    print('\nInserting new node at index 1:')
    my_linked_list.insert(1, 4)

    print('\nLinked List:')
    my_linked_list.printLL()

    print('\nRemoving new node at index 2:')
    my_linked_list.remove(2)

    print('LL before reverse():')
    my_linked_list.printLL()

    my_linked_list.reverse()

    print('\nLL after reverse():')
    my_linked_list.printLL()
