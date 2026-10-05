class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        t =[]
        for x in strs:
            t.append("".join(sorted(x)))
        for i in range(len(strs)):
            key = t[i]
            groups[key].append(strs[i])
        return list(groups.values())
