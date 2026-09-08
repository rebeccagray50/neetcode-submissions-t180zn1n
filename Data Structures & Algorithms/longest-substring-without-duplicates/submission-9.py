class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0 
        actualR = 0 

        for r in range(len(s)):
            #
            if s[r] in mp: 
                #if current val > current l, update
                l = max(mp[s[r]], l)
            
            mp[s[r]] = r
            actualR = max(actualR, (r-l)+1)

        return actualR