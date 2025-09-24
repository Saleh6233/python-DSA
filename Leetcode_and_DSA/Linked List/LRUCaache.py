"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.



Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4


"""


from typing import Optional, Dict, List, Any


class Node:
    """
    Node stored in the doubly-linked list.

    Attributes:
        key: cache key (needed to remove entry from hashmap when evicting)
        val: cached value
        prev: previous Node in the list
        next: next Node in the list
    """

    def __init__(self, key: int, val: int) -> None:
        self.key = key
        self.val = val
        self.prev: Optional["Node"] = None
        self.next: Optional["Node"] = None


class DoublyLinkedList:
    """
    A simple doubly-linked list with two dummy nodes: head and tail.
    We keep most-recently-used nodes near the tail and least-recently-used
    near the head. Dummy nodes simplify insertion/removal logic.

    Key operations:
      - remove(node): unlink a node from the list (O(1))
      - addAtTail(node): append a node just before tail (O(1))
      - removeFromHead(): remove and return the first real node (LRU) (O(1))
    """

    def __init__(self):
        # dummy head and tail to avoid empty-list checks in operations
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node: Node) -> None:
        """
        Unlink `node` from the list.
        Assumes `node` is currently in the list.
        Time: O(1)
        """
        prev_node = node.prev
        next_node = node.next
        # bypass `node`
        if prev_node:
            prev_node.next = next_node
        if next_node:
            next_node.prev = prev_node
        # detach node pointers (helps debugging / prevents accidental reuse)
        node.prev = None
        node.next = None

    def addAtTail(self, node: Node) -> None:
        """
        Insert `node` just before the tail (makes it the most recently used).
        Time: O(1)
        """
        prev_node = self.tail.prev
        # link node between prev_node and tail
        node.next = self.tail
        self.tail.prev = node

        node.prev = prev_node
        if prev_node:
            prev_node.next = node

    def removeFromHead(self) -> Optional[Node]:
        """
        Remove and return the least recently used node (the first real node).
        Returns None if list is empty.
        Time: O(1)
        """
        node_after_head = self.head.next
        if node_after_head == self.tail:
            # list is empty (only dummies present)
            return None
        # unlink and return the real first node
        self.remove(node_after_head)
        return node_after_head


class LRUCache:
    """
    LRU Cache implemented with:
      - a hashmap mapping key -> Node (O(1) lookups)
      - a doubly linked list storing nodes in usage order (LRU at head, MRU at tail)
    Both get and put run in O(1) average time.
    """

    def __init__(self, capacity: int):
        """
        Initialize capacity and supporting structures.
        """
        self.list = DoublyLinkedList()
        self.map: Dict[int, Node] = {}   # maps key -> Node
        self.capacity = capacity

    def getNode(self, key: int) -> Optional[Node]:
        """
        Helper: return the Node for `key` if present, and mark it most-recently-used.
        If not present return None.

        Steps:
          - If key not in map, return None.
          - Otherwise remove the node from its current position and move it to tail.
        Time: O(1)
        """
        if key not in self.map:
            return None

        node_cached = self.map[key]
        # move node to tail (most-recently-used)
        self.list.remove(node_cached)
        self.list.addAtTail(node_cached)
        return node_cached

    def get(self, key: int) -> int:
        """
        Return the value associated with `key` if present; otherwise -1.
        Accessing a key marks it as most recently used.
        Time: O(1)
        """
        node = self.getNode(key)
        return node.val if node else -1

    def put(self, key: int, value: int) -> None:
        """
        Insert or update the value for `key`.
        - If key exists, update the value and mark node MRU.
        - If key doesn't exist, create a node, append at tail (MRU).
          If capacity exceeded, evict the LRU node from head.
        Time: O(1)
        """
        node_existed = self.getNode(key)
        if node_existed:
            # update value (node already moved to MRU by getNode)
            node_existed.val = value
        else:
            self.writeInCache(key, value)

    # ---------- helper functions ----------
    def writeInCache(self, key: int, value: int) -> None:
        """
        Create a new node, insert into map and list at tail (MRU).
        If capacity exceeded, evict the LRU node.
        Time: O(1)
        """
        new_node = Node(key, value)
        self.map[key] = new_node
        self.list.addAtTail(new_node)

        # check capacity and evict LRU if needed
        if len(self.map) > self.capacity:
            self.evictLRU()

    def evictLRU(self) -> None:
        """
        Remove the least recently used node from list and delete its mapping.
        Time: O(1)
        """
        node_removed = self.list.removeFromHead()
        if node_removed and node_removed.key in self.map:
            del self.map[node_removed.key]


# --------------------- Example runner ---------------------
def run_example() -> None:
    """
    Run the example sequence from the prompt and print actual vs expected output.
    """
    ops = ["LRUCache", "put", "put", "get",
           "put", "get", "put", "get", "get", "get"]
    args = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    expected = [None, None, None, 1, None, -1, None, -1, 3, 4]

    outputs: List[Optional[Any]] = []
    cache: Optional[LRUCache] = None

    for op, a in zip(ops, args):
        if op == "LRUCache":
            cache = LRUCache(a[0])
            outputs.append(None)
        elif op == "put":
            assert cache is not None
            cache.put(a[0], a[1])
            outputs.append(None)
        elif op == "get":
            assert cache is not None
            outputs.append(cache.get(a[0]))
        else:
            raise ValueError(f"Unknown operation: {op}")

    print("Actual : ", outputs)
    print("Expected: ", expected)
    print("Match?: ", outputs == expected)


if __name__ == "__main__":
    run_example()
