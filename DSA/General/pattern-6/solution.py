class Solution:
    def pattern6(self, n):

        for i in range(n,0,-1):
            print("".join(str(j) for j in range(1,i+1)))