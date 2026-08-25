class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashset = {}
        output =[]

        for i in numbers:
            hashset[i] = i
        
        for i in hashset:
            if target-i in hashset:
                output.extend([i-1,target-i-1])

                return output


