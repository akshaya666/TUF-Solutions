class Solution:
    def isomorphicString(self, s : str, t : str) -> bool:
        #your code goes here

        s1 = {}

        t1 = {}
        
        if len(s)!= len(t):
            return False

        for i in range(len(s)):

            if s[i] in s1 and s1[s[i]]!=t[i]:

                return False
            if t[i] in t1 and t1[t[i]]!=s[i]:

                return False
            s1[s[i]] = t[i]

            t1[t[i]] = s[i]
        return True






