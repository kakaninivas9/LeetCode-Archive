class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []

        s = sorted(set(arr))
        rank = {}
        for i, x in enumerate(s, 1):
            rank[x] = i

        return list(map(rank.get, arr))