class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0 
        trueR = 0 

        for r in range(len(s)):
            #for each s 
            if s[r] in mp: 
                #edit left 
                l = max(mp[s[r]] + 1, l)
            
            mp[s[r]] = r
            trueR = max(r, (r-l)+1)
        
        return trueR