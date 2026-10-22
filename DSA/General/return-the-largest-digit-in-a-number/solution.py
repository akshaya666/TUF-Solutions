class Solution:
    def largestDigit(self, n):

        largest = 0

        if n <10:
            return n


        while n >0:

            dig = n%10

            if dig > largest:
                largest = dig
            
            n //= 10
        return largest
            