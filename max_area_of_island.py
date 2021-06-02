class Solution:
    visited = {}
    island_locations = {}

    def max_area_of_island(self, grid):
        max_island_size = 0

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                max_island_size = max(max_island_size, self.current_island_size(row, col, grid))
        return max_island_size

    def current_island_size(self, row, col, grid):
        current_location = "{},{}".format(row, col)
        if row < 0 or row >= len(grid) or \
                col < 0 or col >= len(grid[row]) or \
                current_location in self.visited or grid[row][col] == 0:
            return 0

        self.visited[current_location] = True
        return 1 + self.current_island_size(row + 1, col, grid) + \
               self.current_island_size(row - 1, col, grid) + \
               self.current_island_size(row, col + 1, grid) + \
               self.current_island_size(row, col - 1, grid)


if __name__ == "__main__":
    # input_grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    #              [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    #              [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    #             [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

    input_grid = [[1, 1, 0, 1, 1],
                  [1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1],
                  [1, 1, 0, 1, 1]]
    solution = Solution()
    max_area_of_island = solution.max_area_of_island(input_grid)
    print(max_area_of_island)
