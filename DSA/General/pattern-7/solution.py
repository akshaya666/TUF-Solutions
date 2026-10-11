class Solution:
    def pattern7(self, n):

        for i in range(1,n+1):

            space = n-i

            star = 2*i - 1

            print(" "*space+star*"*")