"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""


def twoSum_bruteForce(nums: list[int], target: int) -> list[int]:

    for i in range(len(nums)):

        for j in range(i+1, len(nums)):

            if nums[i] + nums[j] == target:

                return [i, j]


def twoSum_withDict(nums: list[int], target: int) -> list[int]:

    index_visited = {}

    for i in range(len(nums)):

        remaining = target - nums[i]

        if remaining in index_visited:

            return [i, index_visited[remaining]]

        index_visited[nums[i]] = i

    return []


if __name__ == "__main__":
    print(twoSum_bruteForce(nums=[2, 7, 11, 15], target=9))

    print(twoSum_withDict(nums=[2, 7, 11, 15], target=9))
