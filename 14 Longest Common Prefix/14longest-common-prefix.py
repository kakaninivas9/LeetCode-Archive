class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return "".join(c[0] for c in itertools.takewhile(lambda x: len(set(x)) == 1, zip(*strs)))