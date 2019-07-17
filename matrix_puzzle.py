#!/usr/bin/python3
class matrix_puzzle(grid=[][]):
    def __init__(self):
        self.directons = [ [-1, 0], [1, 0], [0, -1], [0, 1] ]
        self.dist2UL = [grid.length()][grid[0].length()] defualt 0
        self.dist2BR = [grid.legnth()][grid[0].length()] default 0
        self.grid = grid
        self.rows = grid.length()
        self.cols = grid[0].length()

    def calculate_shortest(self):
        bfs(self.dist2UL, self.grid, start=[0, 0] end=[self.rows - 1, self.cols -1)
        bfs(self.dist2BR, self.grid, start=[self.rows - 1, self.cols -1), end=[0, 0])
        
        min_step = int().Max_value


        for row in range(0, self.rows):
            for col in range(0, self.cols):
                if grid[row][col] == 1 and dist2UL[row][col] != 0 and dist2BR[row][col] != 0:
                    mininum(min_step, dist2UL[row][col] + dist2BR[row][col])
        #to avoid dist2UL[0][0] and  dist2BR[rows-1][cols-1] equal zero's condition
        if dist2UL[self.rows-1][self.cols-1] != 0:
                    mininum(min_step, dist2UL[self.rows-1][self.cols-1])
        if dist2BR[0][0] != 0:
                    mininum(min_step, dist2BR[0][0])

        if min_step == int().Max_value:
            return None
        else:
            return min_step

    def bfs(self, distArray, grid, start=[], end=[]):
        let Q as stack
        init boolean[rows][cols] visited default False

        
        Q.push(grid[start[0]][start[1]])
        visited[start[0]][start[1]] = True

        step = 0
        while Q is not empty:
                gauge = Q.size()
                for i in range(0, gauge):
                    location_lst = Q.pop(0)
                    row = location_lst[0]
                    col = location_lst[1]
                if grid[row][col] == 1 or row == self.rows - 1 and col == self.cols - 1:
                    distArray[row][col] = step

                for dir_move in self.directions:
                    next_row = row + dir_move[0]
                    next_col = col + dir_move[1]
                    if next_row < 0 || next_col < 0 || next_row > rows || next_col > cols:
                        continue
                    Q.push(grid[next_row][next_col])
                    visited[next_row][next_cow] = True
                step = step + 1 

                
                

