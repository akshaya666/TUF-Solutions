class Solution:
    def isPerfect(self, n: int) -> bool:

        divisiors = []


        for i in range(1,n):

            if n%i == 0:

                divisiors.append(i)

        return sum(divisiors)==n