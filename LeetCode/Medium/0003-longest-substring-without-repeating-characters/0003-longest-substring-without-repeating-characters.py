class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_dict = {}
        max_len = 0
        start = 0

        for i in range(len(s)):
            if s[i] in char_dict:
                start = max(start, char_dict[s[i]] + 1)
            
            char_dict[s[i]] = i
            max_len = max(max_len, i - start + 1)

        return max_len

