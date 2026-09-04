class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0 
        r = len(s)-1

        while l < r: 
            #l and r converge
            #stop on an alphanumeric char, until l passes r
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            #this is the key line 
            #check whether the two are the same
            if s[l].lower() != s[r].lower(): 
                return False
            #increment and repeat
            l, r = l+1, r-1
        #if false condition is never triggered, must be true 
        return True

    #must define your own check for alphanumeric char
    def alphaNum(self, c): 
        #if within range for upper, lower, or nums
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9')
        )
