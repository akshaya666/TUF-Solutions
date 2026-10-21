class Solution:
    def pattern18(self, n):

        for i in range(n):

            start = ord('A')+ n-i-1

            for j in range(i+1):

                print(chr(start+j),end=" ")

            print()

