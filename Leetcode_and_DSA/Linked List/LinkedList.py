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
        return temp.value


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
    print(my_linked_list.pop())

    print('\nHead:', my_linked_list.head.value)
    print('Tail:', my_linked_list.tail.value)
    print('Length:', my_linked_list.length, '\n')
