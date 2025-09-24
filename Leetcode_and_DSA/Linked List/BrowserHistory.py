"""
You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
void visit(string url) Visits url from the current page. It clears up all the forward history.
string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.
 

Example:

Input:
["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
Output:
[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

Explanation:
BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
browserHistory.visit("google.com");       // You are in "leetcode.com". Visit "google.com"
browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"
browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"
browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" return "facebook.com"
browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"
browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.
browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
browserHistory.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"

"""


from typing import Optional, List, Any


class Node:
    """Doubly-linked list node used to store a single URL and links to neighbors."""

    def __init__(self, val: str, prev: Optional["Node"] = None, next: Optional["Node"] = None) -> None:
        self.val = val
        self.prev = prev
        self.next = next


class BrowserHistory:
    """
    BrowserHistory implemented with a doubly-linked list of Node objects.
    - Current page is `self.curr`.
    - Visiting a new URL clears the forward history (nodes after current).
    """

    def __init__(self, homepage: str):
        """
        Initialize browser with homepage as the starting node.
        Time: O(1), Space: O(1)
        """
        self.curr = Node(homepage)

    def visit(self, url: str) -> None:
        """
        Visit `url` from the current page.
        Clears all forward history and appends the new page.
        Time: O(1), Space: O(1)
        """
        # Drop forward history by unlinking any nodes after current.
        # (This makes those nodes unreachable from the current chain and they can be GC'd.)
        if self.curr.next is not None:
            self.curr.next = None

        # Create new node and link it as the next page
        new_node = Node(url, prev=self.curr)
        self.curr.next = new_node
        self.curr = new_node  # move current pointer to the newly visited page

    def back(self, steps: int) -> str:
        """
        Move up to `steps` back in history and return the current URL.
        Time: O(steps), Space: O(1)
        """
        # Walk backwards while we still have steps and a previous node
        while steps > 0 and self.curr.prev is not None:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.val

    def forward(self, steps: int) -> str:
        """
        Move up to `steps` forward in history and return the current URL.
        Time: O(steps), Space: O(1)
        """
        # Walk forwards while steps remain and a next node exists
        while steps > 0 and self.curr.next is not None:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val


# ------------------- Simple runner for the example -------------------
def run_operations(ops: List[str], args: List[List[Any]]) -> List[Optional[str]]:
    """
    Helper that simulates sequence of operations (like the LeetCode input example).
    Returns a list of outputs (None for ctor/visit, string for back/forward).
    """
    outputs: List[Optional[str]] = []
    bh: Optional[BrowserHistory] = None

    for op, a in zip(ops, args):
        if op == "BrowserHistory":
            bh = BrowserHistory(a[0])
            outputs.append(None)
        elif op == "visit":
            assert bh is not None
            bh.visit(a[0])
            outputs.append(None)
        elif op == "back":
            assert bh is not None
            outputs.append(bh.back(a[0]))
        elif op == "forward":
            assert bh is not None
            outputs.append(bh.forward(a[0]))
        else:
            raise ValueError(f"Unknown operation: {op}")

    return outputs


if __name__ == "__main__":
    # Example from the prompt
    ops = ["BrowserHistory", "visit", "visit", "visit", "back",
           "back", "forward", "visit", "forward", "back", "back"]
    args = [["leetcode.com"], ["google.com"], ["facebook.com"], [
        "youtube.com"], [1], [1], [1], ["linkedin.com"], [2], [2], [7]]

    result = run_operations(ops, args)
    print("Outputs:")
    print(result)
    # Expected:
    # [None, None, None, None, "facebook.com", "google.com", "facebook.com",
    #  None, "linkedin.com", "google.com", "leetcode.com"]
