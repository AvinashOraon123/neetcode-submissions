class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = {}
        start_arr =[]
        seq_lengths = []
        for i in nums:
            hashset[i] = i

        for i in hashset:
            if i-1 in hashset:
                continue
            else:
                start_arr.append(hashset[i])
        
        for i in start_arr:
            count = 1
            while i+1 in hashset:
                count+=1
                seq_lengths.append(count)
                i+=1

        return max(seq_lengths)



                

        

        
