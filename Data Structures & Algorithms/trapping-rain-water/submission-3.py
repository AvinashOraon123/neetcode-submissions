class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        max_left = [height[0]] * n
        max_right = [height[-1]] * n

        for i in range(1, n):
            max_left[i] = max(max_left[i-1], height[i])

        for i in range(n-2, -1, -1):
            max_right[i] = max(max_right[i+1], height[i])

        return sum(min(max_left[i], max_right[i]) - height[i] for i in range(n))