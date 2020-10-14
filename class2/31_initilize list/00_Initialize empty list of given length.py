
"""
Init a list with the same content to all elements
"""
arr1=[7]*3

print(arr1) #-> [7, 7, 7]

"""
Init a matrix with the same content to all elements
"""
matrix1=[[7,7]]*3
print(matrix1)   # -> [[7, 7], [7, 7], [7, 7]]

matrix1[0][1]=99

print(matrix1)   # -> [[7, 99], [7, 99], [7, 99]]

matrix2=[[7,7],[7,7],[7,7]]
matrix2[0][1]=99
print(matrix2)   # -> [[7, 99], [7, 7], [7, 7]]