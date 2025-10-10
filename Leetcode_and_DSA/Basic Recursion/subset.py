"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

"""
from typing import List


class Solution:
    """
    A class to find all subsets of a given set of numbers.
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Generates all possible subsets (the power set) from a list of integers.

        This method employs a recursive backtracking algorithm to explore every
        combination of including or not including each element from the input list.

        Args:
            nums: A list of integers. The input numbers can be non-unique,
                  but the standard problem assumes unique elements.

        Returns:
            A list of lists, where each inner list is a unique subset of the
            input list 'nums'. This includes the empty set.
        """
        # 'out' will store the final list of all generated subsets.
        out = []

        def subseq_collect(index: int, current: List[int]):
            """
            A recursive helper function to build subsets.

            For each element in 'nums', this function makes two recursive calls:
            1. One that includes the current element in the subset ("Take").
            2. One that does not include the current element ("Not Take").

            Args:
                index: The current index in the 'nums' list being considered.
                current: The subset being built at the current stage of recursion.
            """
            # Base case: If we have considered all numbers from the input list
            # (i.e., the index is out of bounds), we have formed a complete subset.
            if index >= len(nums):
                # We add a copy of the 'current' subset to our output list.
                # A copy is essential because 'current' is a mutable list that
                # will be modified as we backtrack up the recursion tree.
                out.append(current.copy())
                return

            # --- Recursive Step 1: "Take" the element ---
            # Include the number at the current index in our subset.
            current.append(nums[index])
            # Recursively call the function to explore subsets with this number included.
            # We move to the next index (index + 1).
            subseq_collect(index + 1, current)

            # --- Recursive Step 2: "Not Take" the element (Backtrack) ---
            # Remove the number we just added to backtrack. This step is crucial.
            # It allows us to explore the path where we DON'T include the current element.
            current.pop()
            # Recursively call the function again, but this time without the current number.
            subseq_collect(index + 1, current)

        # Start the recursion from the first element (index 0) with an empty initial subset.
        subseq_collect(0, [])

        # Return the final list containing all subsets.
        return out


# This block allows the script to be run directly to test the solution.
if __name__ == "__main__":
    # Create an instance of the Solution class.
    solver = Solution()

    # Define a sample input list of numbers.
    input_nums = [1, 2, 3]

    # Call the subsets method to get the power set.
    result = solver.subsets(input_nums)

    # Print the results in a readable format.
    print(f"Input numbers: {input_nums}")
    print(f"All possible subsets (Power Set):")
    # The result contains lists, which can be sorted for a canonical output order.
    # Sorting each subset and then sorting the list of subsets makes the output consistent.
    result.sort(key=lambda x: (len(x), x))
    print(result)

    # Example with an empty list
    input_empty = []
    result_empty = solver.subsets(input_empty)
    print(f"\nInput numbers: {input_empty}")
    print(f"All possible subsets: {result_empty}")
