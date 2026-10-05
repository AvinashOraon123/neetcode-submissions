class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = [-1] * 128     
        l = 0
        res = 0
        for r, ch in enumerate(s):
            c = ord(ch)
            if last[c] >= l:   
                l = last[c] + 1
            last[c] = r
            res = max(res, r - l + 1)
        return res