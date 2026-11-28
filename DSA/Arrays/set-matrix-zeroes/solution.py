class Solution:
    def setZeroes(self, matrix):

        # Your code goes here


        frist_row , firxt_col = False, False

        for i in range(len(matrix[0])):

            if matrix[0][i]==0:
                frist_row = True
                break
        for j in range(len(matrix)):

            if matrix[j][0] == 0:
                firxt_col = True
                break
            
        for i in range(1,len(matrix)):

            for j in range(1,len(matrix[0])):

                if matrix[i][j] == 0:

                    matrix[i][0],matrix[0][j] = 0,0
        
        for i in range(1,len(matrix)):

            for j in range(1,len(matrix[0])):

                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if frist_row:

            for i in range(len(matrix[0])):

                matrix[0][i] = 0

        if firxt_col:

            for j in range(len(matrix)):

                matrix[j][0] = 0
        return matrix



