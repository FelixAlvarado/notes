# Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

# Return the number of closed islands.

 

# Example 1:



# Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
# Output: 2
# Explanation: 
# Islands in gray are closed because they are completely surrounded by water (group of 1s).
# Example 2:



# Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
# Output: 1
# Example 3:

# Input: grid = [[1,1,1,1,1,1,1],
#                [1,0,0,0,0,0,1],
#                [1,0,1,1,1,0,1],
#                [1,0,1,0,1,0,1],
#                [1,0,1,1,1,0,1],
#                [1,0,0,0,0,0,1],
#                [1,1,1,1,1,1,1]]
# Output: 2


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        # our helper function to see if with the current grid node, we could get
        # a closed island
        def isClosed(r, c):
            # at first we check if it is already a visited or is 1 (water)
            # means we are still on the way of a close island
            # so we return true from here
            if grid[r][c] == -1 or grid[r][c] == 1:
                return True
            # if we pass the above if, it means we see a 0 (land)
            # we need to check if that 0 in the perimeter of the given grid
            # if it is in the perimeter means there is no way, this island so far
            # is going to be a closed island. So we return False.
            if r == 0 or r == rows-1 or c == 0 or c == cols -1:
                return False
            # if we pass the above if, means we are still on the way to get a close 
            # island. So marking the node as visited
            grid[r][c] = -1
            
            # now recurse on the four adjacent neighbors
            up = isClosed(r-1,c)
            down = isClosed(r+1,c)
            left = isClosed(r,c-1)
            right = isClosed(r,c+1)
            
            return up and down and left and right
            
            
        # get the number of rows and columns
        rows = len(grid)
        if not rows:
            return 0
        cols = len(grid[0])
        # we will start checking for land from the inside, excluding perimeter cell
        # of the given grid matrix. So we start working on a sub-grid
        num_distinct = 0
        for r in range(1, rows-1):
            for c in range(1, cols -1):
                # if we see a 0 (land) we start exploring for a possible closed island 
                if grid[r][c] == 0:
                    if isClosed(r,c): # if the helper function return True
                        num_distinct += 1 # increase the number of closed island
        return num_distinct