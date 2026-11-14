class Solution:
    def mostFrequentElement(self, nums):

        mp = {}

        cnt = -1

        ans = -1

        for i in nums:

            mp[i] = mp.get(i,0) + 1

            if cnt < mp[i]:
                cnt = mp[i]
                if ans != i:
                    ans = i
            
            elif cnt == mp[i]:
                if i < ans:
                    ans = i

                
        return ans

             