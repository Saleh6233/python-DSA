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
    def reverseString(self, s: List[str]) -> None:
        """
        Reverse the list `s` in-place.

        Parameters
        ----------
        s : List[str]
            A list of single-character strings (e.g., ['h','e','l','l','o']).

        Returns
        -------
        None
            The list is modified in-place; nothing is returned (function returns None).

        Algorithm (two-pointer swap)
        ----------------------------
        - Maintain two pointers, `left` starting at 0 and `right` starting at len(s)-1.
        - While left < right:
            - Swap the elements at left and right.
            - Move left forward and right backward.
        - This reverses the list in-place using constant extra memory.

        Example
        -------
        >>> s = ['h', 'i']
        >>> Solution().reverseString(s)
        >>> print(s)
        ['i', 'h']
        """
        # Initialize two pointers to the ends of the list
        left = 0
        right = len(s) - 1

        # Loop until the pointers meet or cross
        while left < right:
            # Save right element temporarily, copy left to right, then put temp in left.
            # This is the standard three-statement swap; we could also use tuple swap:
            #     s[left], s[right] = s[right], s[left]
            # but we keep the explicit temp here to make the steps clear.
            temp = s[right]
            s[right] = s[left]
            s[left] = temp

            # Move pointers inward
            left += 1
            right -= 1


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
