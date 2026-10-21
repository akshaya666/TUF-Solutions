class Solution:
    def countOddDigit(self, n):

        count = 0

        if n < 10:

            if n%2 == 0:
                return 0
            else:
                return 1
        
        while n>0:

            rem = n % 10

            if rem % 2 != 0:
                count += 1
            
            n //= 10
        
        return count

