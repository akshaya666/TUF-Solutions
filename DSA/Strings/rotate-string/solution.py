class Solution:    
    def rotateString(self, s, goal):
        #your code goes here


        combined = s + s

        if len(s) != len(goal):
            return False 
        
        return goal in combined