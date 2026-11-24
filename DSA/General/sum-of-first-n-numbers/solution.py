class Solution:
    def NnumbersSum(self, N):
        #your code goes here

        if N == 1 or N == 0:

            return N
        
        return N + self.NnumbersSum(N-1)
