#!/usr/bin/python3
""" Module for pascal's triangle"""


def pascal_triangle(n):
    """
  This function generates Pascal's triangle up to n rows.

  Args:
      n: An integer representing the number of rows in the triangle.

  Returns:
      A list of lists containing the integers of Pascal's triangle.
      Returns an empty list if n <= 0.
  """

    triangle = []
    if n <= 0:
        return triangle

    # Add the first row (always [1])
    triangle.append([1])

    # Iterate for remaining rows
    for i in range(1, n):
        row = [1]  # Every row starts and ends with 1
        # Calculate elements using elements from the previous row
        for j in range(1, i):
            prev_row = triangle[i - 1]
            element = prev_row[j - 1] + prev_row[j]
            row.append(element)
        row.append(1)  # Last element is always 1
        triangle.append(row)

    return triangle
