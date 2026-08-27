class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashset = {}
        output =[]

        for i in numbers:
            hashset[i] = i
        
        for i in hashset:

            if target-i in hashset:
                keys = [k for k, v in hashset.items() if v == i or v == target-i]
                output.extend(keys)

                return output

