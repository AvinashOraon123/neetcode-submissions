class Solution:
    def trap(self, height: List[int]) -> int:
        #O(n) space solution 
        max_left = [0]*len(height)
        max_right = [0]*len(height)
        min_l_r = [0]*len(height)
        res = 0

        for i in range(1, len(height)):
            #max_left[0] = 0
            max_left[i] = max(max_left[i-1], height[i] )
        
        for i in range(len(height)-2, 0 ,-1):
            #max_right[len(height)-1] = 0
            max_right[i] = max(max_right[i+1], height[i] )

        for i in range(0, len(height)):
            min_l_r[i] = min(max_left[i], max_right[i])

        for i in range(0, len(height)):
            res+= max(min_l_r[i] - height[i], 0 )

        return res