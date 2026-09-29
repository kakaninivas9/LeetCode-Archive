class Solution:
    def reverseParentheses(self, s: str) -> str:
        answer = [""]
        for c in s:
            if c == "(":
                answer.append("")
            elif c == ")":
                w = answer.pop()[::-1]
                answer[-1] += w
            else:
                answer[-1] += c
        return answer[0]