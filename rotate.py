#思想是： 先矩阵的转置，再翻转每一行

def rotate(matrix):
    cols = len(matrix[0])
    for i in range(cols):
        for j in range(i,cols):
            matrix[j][i],matrix[i][j] = matrix[i][j],matrix[j][i]
    
    for i in range(cols):
        matrix[i].reverse()
    return matrix

matrix =[[ 5, 1, 9,11],[ 2, 4, 8,10],[13, 3, 6, 7],[15,14,12,16]]
print(rotate(matrix))
