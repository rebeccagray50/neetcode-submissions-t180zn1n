class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0 
        r = 0

        for i in range(len(s)):
            while s[i] in charSet: 
                l += 1
            charSet.add(s[i])
            r = max(r, (i -1 + 1))

        return r