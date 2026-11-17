class Solution: 
    def reverseString(self, s):
        #your code goes here

        n = len(s)

        left,right = 0,n-1

        while left < right:

            s[left], s[right] = s[right], s[left]

            left +=1
            right-=1
        