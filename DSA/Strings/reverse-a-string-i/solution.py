class Solution:
    def reverseString(self,s):
        #your code goes here

        self.helper(s,0,len(s)-1)

        return s


    
    def helper(self,s,left,right):

        if left >= right:
            return

        s[left], s[right] = s[right], s[left]


        self.helper(s,left+1,right-1)

