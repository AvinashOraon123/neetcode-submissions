class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            hash_map[nums[i]] = i

        for i in range(len(nums)):
            j = hash_map.get(target - nums[i])
            if j is not None and j != i:
                return [i, j]