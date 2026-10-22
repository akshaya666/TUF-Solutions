class Solution:
    def isPalindrome(self, n):

        
        if n < 10:

            return True;
        
        rev = 0
        temp = n
        while temp > 0:

            dig = temp % 10

            rev = rev *10 + dig

            temp //= 10
        
        return rev==n



