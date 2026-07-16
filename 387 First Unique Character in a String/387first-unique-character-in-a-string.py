class Solution:
    def firstUniqChar(self, s: str) -> int:
        result = len(s)
        for i in 'abcdefghijklmnopqrstuvwxyz':
            first = s.find(i)
            if first!=-1 and first==s.rfind(i):
                if first<result:
                    result = first

        return result if result!=len(s) else -1