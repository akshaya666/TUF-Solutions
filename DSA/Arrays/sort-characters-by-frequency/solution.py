class Solution:
    def frequencySort(self, s):
        #your code goes here

        freq = {}

        for i in s:
            freq[i] = freq.get(i,0) + 1

        result = sorted(freq,key = lambda x: (-freq[x],x))

        return result
