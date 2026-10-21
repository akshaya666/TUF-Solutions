class Solution:
    def reverseNumber(self, n):

        s = ""

        if n < 10:

            return n
        
        while n > 0:

            digit = n % 10

            s += str(digit)

            n //= 10
        
        ans = int(s)

        return ans



