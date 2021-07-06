from typing import List

def rotate(self, matrix: List[List[int]]) -> None:
    l=len(matrix[0])
    #Transposing matrix.you can also use numpy library to transpose the matrix
    for row in range(l):
        for col in range(row,l):
            matrix[col][row], matrix[row][col] = matrix[row][col], matrix[col][row]
    
    
    for i in range(l):
        matrix[i].reverse()
        
    return matrix


print(rotate(self=1,matrix=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))