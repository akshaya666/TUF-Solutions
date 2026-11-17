class Solution:  
    def largeOddNum(self, s: str) -> str:
        #your code goes here

        dig = -1

        for i in range(len(s)-1,-1,-1):

            if int(s[i]) %2 ==1:

                return s[:i+1].lstrip('0')
            
        return ""