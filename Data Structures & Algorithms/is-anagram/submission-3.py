class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #sort chars into order, then check if they are same
        mapS = {}
        mapT = {}

        if len(s) != len(t):
            return False
        
        #add each letter to the freq. map
        for i in range(0, len(s)):
            mapS[s[i]] = mapS.get(s[i], 0) + 1
            mapT[t[i]] = mapT.get(t[i], 0) + 1

        
        if mapS == mapT: 
            return True
        else: 
            return False