"""
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
"""

def rotate_matrix(matrix)
# REVERSING THE MATRIX
    left = 0
    right = len(matrix) - 1
    while left < right:
        matrix[left], matrix[right] = matrix[right], matrix[left]
        left += 1
        right -= 1

    #Calculating the transpose of the matrix
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# this is going to be O(n^2)in time
# this would be O(1) in space cz we aren't using any extra data structure to store anything
