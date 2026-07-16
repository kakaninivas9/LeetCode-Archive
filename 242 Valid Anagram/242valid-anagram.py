class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_s = Counter(s)
        dict_t = Counter(t)
        for i in dict_s:
            if dict_s[i] != dict_t[i]:
                return False
        return True