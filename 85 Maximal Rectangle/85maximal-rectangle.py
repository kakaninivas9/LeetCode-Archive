from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        def largestRectangle(heights):
            stack = []
            ans = 0
            heights.append(0)

            for i, h in enumerate(heights):
                while stack and heights[stack[-1]] > h:
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    ans = max(ans, height * width)
                stack.append(i)

            heights.pop()
            return ans

        n = len(matrix[0])
        heights = [0] * n
        ans = 0

        for row in matrix:
            for j in range(n):
                if row[j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0
            ans = max(ans, largestRectangle(heights))

        return ans