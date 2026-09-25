class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        left = 0 
        finalRight = 0 

        for right in range(len(s)):
            #check whether in chars
            if s[right] in chars:
                #change left 
                #to be either: current left, or index at which rightmost value appeared

                left =  max(left, (chars[s[right]] + 1))

            #change char value to represent last place it appeared 
            chars[s[right]] = right
            #then update finalRight
            finalRight = max(finalRight, (right-left)+1)

        return finalRight