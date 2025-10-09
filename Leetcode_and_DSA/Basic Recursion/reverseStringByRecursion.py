"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.



Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""


from typing import List


class Solution:

    def swap(self, s: list[str], left: int, right: int) -> None:

        if left >= right:
            return

        temp = s[right]
        s[right] = s[left]
        s[left] = temp

        self.swap(s, left=left+1, right=right-1)

    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1

        self.swap(s, left, right)


def demo_examples() -> None:
    """Run a few example cases and print before/after states."""
    examples = [
        (['h', 'e', 'l', 'l', 'o'], "odd length"),
        (['H', 'i'], "even length"),
        ([], "empty list"),
        (['a'], "single element"),
    ]

    solver = Solution()
    for arr, desc in examples:
        # Make a shallow copy for display so we can show before/after
        before = arr.copy()
        solver.reverseString(arr)  # modifies `arr` in-place
        print(f"{desc:12} | before: {before} -> after: {arr}")


if __name__ == "__main__":
    demo_examples()
