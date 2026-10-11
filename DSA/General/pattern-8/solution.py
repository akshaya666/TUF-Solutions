class Solution:
    def pattern8(self, n):

        for i in range(n,0,-1):

            space = n-i
            star = 2*i-1

            print(" "*space+"*"*star)