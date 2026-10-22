class Solution:
    def isPrime(self, n):
        #your code goes here

        if n==1:
            return False

        for i in range(1,n):

            if n%i ==0 and i!=1:
                return False
        return True