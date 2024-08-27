#!/usr/bin/python3
def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.

    Parameters:
    grid (List[List[int]]): 2D grid where 1 represents land
        and 0 represents water.

    Returns:
    int: The perimeter of the island.
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check the four directions
                if i == 0 or grid[i-1][j] == 0:  # Up
                    perimeter += 1
                if i == rows - 1 or grid[i+1][j] == 0:  # Down
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:  # Left
                    perimeter += 1
                if j == cols - 1 or grid[i][j+1] == 0:  # Right
                    perimeter += 1

    return perimeter
