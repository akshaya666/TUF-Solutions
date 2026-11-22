class Solution:    
    def anagramStrings(self, s, t):
        #your code goes here

        freq = {}

        if len(s) != len(t):

            return False

        for i in s:

            freq[i] = freq.get(i,0)+1
            
        for j in t:

            freq[j] = freq.get(j,0) -1

        
        for k,v in freq.items():

            if v!=0:
                return False
        return True


