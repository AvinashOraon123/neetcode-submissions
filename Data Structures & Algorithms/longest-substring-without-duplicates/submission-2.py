class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        len_longest = 0 

        l,r = 0,0
        while r<len(s):
            while s[r] in char_set:
                char_set.remove(s[l])
                l+=1
            char_set.add(s[r])
            r+=1
            len_longest = max(len_longest,r-l)
           

        return len_longest