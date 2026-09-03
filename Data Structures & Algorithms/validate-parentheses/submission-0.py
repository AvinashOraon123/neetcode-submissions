class Solution:
    def isValid(self, s: str) -> bool:

        hashmap = {
            '(':')',
            '[':']',
            '{':'}'
        }
        l,r = 0, len(s)-1
        while l<r:
            if hashmap[s[l]] == s[r]:
                l+=1
                r-=1
            else:
                return False

        return True

        