"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

"""


def majorityElement_withDict(nums: list[int]) -> int:

    count_map = {}

    for num in nums:

        if num not in count_map:
            count_map[num] = 1

        else:

            count_map[num] = count_map[num] + 1

    for num, count in count_map.items():

        if count > (len(nums) / 2):
            return num

    return 0


def majorityElement_withSort(nums: list[int]) -> int:

    nums.sort()

    mid = int(len(nums)/2)

    return nums[mid]


def majorityElement_withVote(nums: list[int]) -> int:

    top_can = -1

    count = 0

    for curr in nums:

        if count == 0:
            top_can = curr

        if top_can == curr:

            count += 1

        else:

            count -= 1

    return top_can


if __name__ == "__main__":
    print(majorityElement_withDict(nums=[2, 2, 1, 1, 1, 2, 2]))

    print(majorityElement_withSort(nums=[2, 2, 1, 1, 1, 2, 2]))

    print(majorityElement_withVote(nums=[2, 2, 1, 1, 1, 2, 2]))
