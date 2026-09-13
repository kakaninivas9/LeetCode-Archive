from collections import Counter

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        A = []
        B = []

        n = len(img1)

        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    A.append((i, j))
                if img2[i][j] == 1:
                    B.append((i, j))

        count = Counter()

        for x1, y1 in A:
            for x2, y2 in B:
                count[(x1 - x2, y1 - y2)] += 1

        return max(count.values(), default=0)