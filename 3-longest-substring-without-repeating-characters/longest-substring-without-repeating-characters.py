class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current = ""
        longest = 0
        for ch in s:
            if ch in current:
                current = current[current.index(ch) + 1:]
            current += ch
            longest = max(longest, len(current))
        return longest
