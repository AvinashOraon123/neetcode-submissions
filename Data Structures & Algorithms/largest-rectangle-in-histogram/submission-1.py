from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []  # Pairs: (earliest start index, height)

        for i, height in enumerate(heights):
            start = i

            while stack and stack[-1][1] > height:
                index, previous_height = stack.pop()
                max_area = max(max_area, previous_height * (i - index))
                # The shorter bar can extend across the popped bars.
                start = index

            stack.append((start, height))

        # Remaining bars can extend to the end of the histogram.
        n = len(heights)
        for start, height in stack:
            max_area = max(max_area, height * (n - start))

        return max_area
