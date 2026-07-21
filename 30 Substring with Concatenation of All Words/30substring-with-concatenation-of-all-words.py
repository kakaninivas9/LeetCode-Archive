from collections import defaultdict, Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        wlen = len(words[0])
        total_words = len(words)
        total_len = wlen * total_words
        
        if len(s) < total_len:
            return []

        target = Counter(words)
        ans = []

        # Iterate over each possible starting offset
        for offset in range(wlen):
            left = offset
            right = offset
            window = defaultdict(int)
            count = 0

            while right + wlen <= len(s):
                word = s[right:right + wlen]
                right += wlen

                if word in target:
                    window[word] += 1
                    count += 1

                    # If there are too instances of a word, shrink the window from the left
                    while window[word] > target[word]:
                        left_word = s[left:left + wlen]
                        window[left_word] -= 1
                        left += wlen
                        count -= 1

                    # If we match all words, record the valid starting index
                    if count == total_words:
                        ans.append(left)
                        # Slide past the first word to look for subsequent overlapping/adjacent matches
                        left_word = s[left:left + wlen]
                        window[left_word] -= 1
                        left += wlen
                        count -= 1
                else:
                    # Reset window completely when an invalid word breaks the sequence
                    window.clear()
                    count = 0
                    left = right

        return ans