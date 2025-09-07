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
