class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        while numSet:
            n = numSet.pop()
            lo = hi = n
            while lo - 1 in numSet:
                lo -= 1
                numSet.remove(lo)
            while hi + 1 in numSet:
                hi += 1
                numSet.remove(hi)
            longest = max(longest, hi - lo + 1)
            if longest >= len(numSet):   # remaining numbers can't beat it
                break
        return longest