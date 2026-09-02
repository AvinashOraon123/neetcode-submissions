class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        result = []
        while l<r:
            if numbers[l]+ numbers[r] == target:
                result.extend([l+1,r+1])
                return result
            if numbers[l]+ numbers[r] > target:
                r-=1
            if numbers[l]+ numbers[r] < target:
                l+=1
        return 'no such two numbers'


