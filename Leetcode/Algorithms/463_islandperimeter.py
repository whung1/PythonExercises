"""
https://leetcode.com/problems/island-perimeter
"""
from collections import deque


def island_perimeter_dfs_visited(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """

    def find_first(grid):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    return (i, j)
    stack = deque()
    stack.append(find_first(grid))
    visited = set()
    perimeter = 0
    while stack:
        x, y = stack.pop()
        if (x,y) not in visited:
            visited.add((x,y))
            neighbors = (x+1, y), (x-1, y), (x, y+1), (x, y-1)
            cur_perimeter = 4  # a perimeter starts with four for a lone island and subtracts for each neighbor
            for i, j in neighbors:
                if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == 1:
                    cur_perimeter -= 1
                    stack.append((i, j))
            perimeter = perimeter + cur_perimeter
    return perimeter


def island_perimeter_brute(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    count = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 1:
                neighbors = (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)
                for i, j in neighbors:
                    if len(grid) <= i or i < 0 or len(grid[i]) <= j or j < 0 or grid[i][j] == 0:
                        count += 1
    return count

if __name__ == "__main__":
    print("""
    You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. 
    Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). 
    The island doesn't have "lakes" (water inside that isn't connected to the water around the island). 
    One cell is a square with side length 1. 
    The grid is rectangular, width and height don't exceed 100. 
    Determine the perimeter of the island.

    Example:

    [[0,1,0,0],
     [1,1,1,0],
     [0,1,0,0],
     [1,1,0,0]]

    Answer: 16
    Explanation: The perimeter is the 16 yellow stripes in the image below:
    """)

    print(island_perimeter_dfs_visited([[0,1,0,0],
                         [1,1,1,0],
                         [0,1,0,0],
                         [1,1,0,0]]))
    print(island_perimeter_dfs_visited([[1,1],[1,1]]))

    print(island_perimeter_brute([[0,1,0,0],
                         [1,1,1,0],
                         [0,1,0,0],
                         [1,1,0,0]]))
    print(island_perimeter_brute([[1,1],[1,1]]))
    print(island_perimeter_brute([[1]]))
