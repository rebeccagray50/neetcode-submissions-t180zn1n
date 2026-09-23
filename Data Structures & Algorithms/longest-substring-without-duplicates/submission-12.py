class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        finalR = 0

        for r in range(len(s)):
            
            if s[r] in mp: 
                l = max(l, (mp[r]+1))

            mp[s[r]] = r
            finalR = max(finalR, (r-l)+1)
        
        return finalR
                