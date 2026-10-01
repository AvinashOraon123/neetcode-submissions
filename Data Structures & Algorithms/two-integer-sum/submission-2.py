class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i in range(len(nums)):
            hash_map[nums[i]] = i

        for n in nums:
            if target-n in hash_map:
                return [hash_map[n], hash_map[target-n]]
            
        