class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = {}
        l, r = 0 ,0 
        res = 0 
        while r < len(s):
            window_len = r-l+1
            max_count = max(hash_map.values(), default=0)
            if s[r] not in hash_map:
                hash_map[s[r]] = 1
            else:
                hash_map[s[r]]+=1
            if window_len - max_count <=k:
                r+=1
                res=max(res,window_len)
            else:
                hash_map[s[l]]-=1
                l+=1

        return res