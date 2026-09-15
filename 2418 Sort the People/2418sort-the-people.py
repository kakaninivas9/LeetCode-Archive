class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        p = sorted(zip(heights, names), reverse=True)
        return [name for h, name in p]