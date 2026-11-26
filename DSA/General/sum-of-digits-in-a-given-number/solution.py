class Solution:
    def addDigits(self, num):
        #your code goes here

        if num < 10:
            return num 
        
        total = 0

        while num > 0:

            digit = num % 10 

            total += digit

            num //= 10
        
        return self.addDigits(total)

