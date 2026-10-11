class Solution:
    def pattern11(self, n):

        for i in range(1,n+1):

            num = 1 if i%2 != 0 else 0

            for j in range(i):
                if j !=i-1:
                    print(num,end=" ")
                else:
                    print(num,end="")
                num =1- num
            print()