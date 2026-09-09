class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqS = [0] * 26
        freqT = [0] * 26

        if len(s) != len(t):
            return False 

        for i in range(len(s)):
            freqS[ord('a') - ord(s[i])] += 1 
            freqT[ord('a') - ord(t[i])] += 1
        
        if freqS == freqT: 
            return True
        else: 
            return False 




