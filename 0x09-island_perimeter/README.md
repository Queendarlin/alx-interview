# Island Perimeter

## Overview

The "Island Perimeter" project involves calculating the perimeter of an island in a 2D grid. The grid is represented by a list of lists where:
- `0` represents water.
- `1` represents land.

The island is completely surrounded by water, and there are no lakes (water inside the island not connected to the surrounding water).

## Function

### `island_perimeter(grid)`

Calculates the perimeter of the island in the given grid.

**Parameters:**
- `grid` (List[List[int]]): A 2D list where `1` represents land and `0` represents water.

**Returns:**
- `int`: The perimeter of the island.

**Example:**
```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
print(island_perimeter(grid))  # Output: 12

