class Solution:

    def pattern19(self, n):

        for i in range(n):

            print("*"*(n-i)+ (2*i)*" " + "*"*(n-i))

        for i in range(n):

            print("*"*(i+1)+ (2*(n-i-1))*" " + "*"*(i+1))