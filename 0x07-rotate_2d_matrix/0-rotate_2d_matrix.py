#!/usr/bin/python3
"""
Rotate an n x n 2D matrix 90 degrees clockwise in-place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate the given n x n matrix 90 degrees clockwise in-place.

    :param matrix: List[List[int]] - A 2D list representing the matrix.
    :return: None - The matrix is rotated in place.
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
