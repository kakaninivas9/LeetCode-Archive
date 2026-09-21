class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        for ch in letters:
            if ch > target:
                return ch
        return letters[0]