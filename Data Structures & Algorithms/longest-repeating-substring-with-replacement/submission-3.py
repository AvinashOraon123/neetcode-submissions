class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = {}
        l, r = 0 ,0 
        res = 0 
        while r < len(s):
            hash_map[s[r]] = hash_map.get(s[r], 0) + 1
            window_len = r-l+1
            max_count = max(hash_map.values(), default=0)
            
            if window_len - max_count <=k:
                res=max(res,window_len)
            else:
                hash_map[s[l]]-=1
                l+=1
            r+=1
        return res