"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

"""


from typing import Tuple


class Solution:
    def check_palin(self, s: str, left: int, right: int) -> bool:
        """
        Recursively check whether the substring s[left:right+1] is a palindrome.

        Base case:
            - If left >= right, we've compared all necessary character pairs (or the
              substring length is 0/1), so it's a palindrome.

        Recursive step:
            - If the characters at 'left' and 'right' differ, it's not a palindrome.
            - Otherwise, move inward by calling check_palin(s, left+1, right-1).

        Parameters
        ----------
        s : str
            The cleaned string (only lowercase alphanumerics).
        left : int
            Left index of the substring to check (inclusive).
        right : int
            Right index of the substring to check (inclusive).

        Returns
        -------
        bool
            True if s[left:right+1] is a palindrome, False otherwise.
        """
        # Base case: crossed indices or single character -> palindrome
        if left >= right:
            return True

        # If characters at the two ends are different -> not a palindrome
        if s[left] != s[right]:
            return False

        # Characters match -> check the inner substring
        return self.check_palin(s, left + 1, right - 1)

    def isPalindrome(self, s: str) -> bool:
        """
        Public method to check if the input string s is a palindrome under the
        problem rules:
          - ignore non-alphanumeric characters
          - ignore case (case-insensitive)

        Steps:
          1. Clean the string: keep only alphanumeric chars and normalize case using
             casefold() (more aggressive than lower() for some Unicode cases).
          2. Call the recursive checker on the cleaned string.

        Complexity:
          - Time: O(n) to build the cleaned string + O(n) for recursion checks => O(n).
          - Space: O(n) for the cleaned string + O(n) recursion stack => O(n).
        """
        # Build a cleaned version of the string:
        # - ch.isalnum() filters to alphanumeric characters (letters and digits).
        # - ch.casefold() normalizes case for robust, locale-independent comparisons.
        cleaned = ''.join(ch.casefold() for ch in s if ch.isalnum())

        # Important: pass the length of the cleaned string, not the original string.
        # Using len(s) here was the source of the IndexError you saw earlier.
        return self.check_palin(cleaned, left=0, right=len(cleaned) - 1)


# Example usage / quick manual tests
if __name__ == "__main__":
    sol = Solution()

    tests = (
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),                     # becomes "" after cleaning -> palindrome
        ("0P", False),                   # different characters
        ("Able was I, ere I saw Elba", True),
    )

    for inp, expected in tests:
        got = sol.isPalindrome(inp)
        print(f"Input: {inp!r}\nExpected: {expected}, Got: {got}\n")
