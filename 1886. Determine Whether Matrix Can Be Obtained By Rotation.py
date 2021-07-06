from typing import List
def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        def rotate(matrix: List[List[int]]) -> List[int]:
            l=len(matrix[0])
            #Transposing matrix.you can also use numpy library to transpose the matrix
            for row in range(l):
                for col in range(row,l):
                    matrix[col][row], matrix[row][col] = matrix[row][col], matrix[col][row]


            for i in range(l):
                matrix[i].reverse()

            return matrix

        
        
        rotated=mat
        for i in range(4):
            rotated = rotate(matrix=rotated)
            if(rotated==target):
                return True

        return False

print(findRotation(self=2,mat=[[0,0,0],[0,1,0],[1,1,1]],target=[[1,1,1],[0,1,0],[0,0,0]]))