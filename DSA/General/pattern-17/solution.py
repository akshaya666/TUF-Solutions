class Solution:
    def pattern17(self, n):

        for i in range(n):

            space = n-i-1

            print(space*" ",end="")

            for j in range(i+1):

                print(chr(ord('A')+j),end="")
            
            for k in range(i-1,-1,-1):

                print(chr(ord('A')+k),end="")
            print()