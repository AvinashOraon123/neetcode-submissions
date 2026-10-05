class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        l=0
        while l<=len(s2)-window_size:
            test_str = s2[l:l+window_size]
            if sorted(test_str) == sorted(s1):    
                return True
            l+=1
        return False

    