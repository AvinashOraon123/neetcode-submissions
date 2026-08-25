class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashset = {}
        output =[]

        for i in numbers:
            hashset[i] = numbers.index(i)+1
        
        for i in hashset.keys():
            if target-i in hashset.keys():
                output.extend([hashset[i],hashset[target-i]])

                return output


