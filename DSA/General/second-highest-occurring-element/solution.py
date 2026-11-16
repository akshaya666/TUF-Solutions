class Solution:
    def secondMostFrequentElement(self, nums):

        freq = {}

        for i in nums:

            freq[i]= freq.get(i,0)+1
        
        max_1,max_2 = -1,-1

        cnt_1,cnt_2 = 0,0

        for num,count in freq.items():

            if count > cnt_1:

                cnt_2 = cnt_1

                cnt_1 = count

                max_2 = max_1

                max_1 = num
            
            elif count == cnt_1:

                max_1 = min(max_1,num)
            
            elif count > cnt_2:

                max_2 = num 

                cnt_2 = count

            elif count == cnt_2:

                max_2 = min(max_2,num)
            
        return max_2
            

