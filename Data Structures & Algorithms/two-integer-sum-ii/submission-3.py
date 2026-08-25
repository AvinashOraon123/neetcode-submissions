class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashset = {}
        output =[]

        for i in numbers:
            hashset[i] = numbers.index(i)+1
        
        for i in hashset:
            if target-i in hashset:
                output.extend([i,target-i])

                return output


