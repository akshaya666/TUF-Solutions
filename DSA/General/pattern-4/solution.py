class Solution:
    def pattern4(self, n):

        for i in range(1,n+1):
            print("".join(str(i) for j in range(1,i+1)))