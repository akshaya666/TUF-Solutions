class Solution:
    def pattern12(self, n):

        for i in range(1,n+1):


            for l in range(1,i+1):
                print(l,end="")

            space = 2*(n-i)

            print(space*" ",end="")

            for r in range(i,0,-1):
                print(r,end="")
            
            print()