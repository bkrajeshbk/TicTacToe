class Board:
    def __init__(self) -> None:
        """ This function initialises the grid, when this class gets instantiated. """
        self.grid = [None for _ in range(9)]

    def __str__(self) -> str:
        """ This function returns the grid with current values in 3X3 format. """
        output_grid = ""
        space_count = 0
        for value in self.grid:
            output_grid += str(value) + " "
            space_count += 1
            if space_count == 3:
                output_grid += "\n"
                space_count = 0
        return output_grid

    def check_result(self):
        """ This function evaluates if any 3 consecutive slots are filled with the same symbol. If so returns that symbol. """
        if self.grid[0] is not None and (self.grid[0] == self.grid[1] == self.grid[2] \
            or self.grid[0] == self.grid[3] == self.grid[6] \
                or self.grid[0] == self.grid[4] == self.grid[8]):
            return self.grid[0]
        
        if self.grid[1] is not None and self.grid[1] == self.grid[4] == self.grid[7]:
            return self.grid[1]
        
        if self.grid[2] is not None and (self.grid[2] == self.grid[4] == self.grid[6] \
            or self.grid[2] == self.grid[5] == self.grid[8]):
            return self.grid[2]

        if self.grid[3] is not None and self.grid[3] == self.grid[4] == self.grid[5]:
            return self.grid[4]
        
        if self.grid[6] is not None and self.grid[6] == self.grid[7] == self.grid[8]:
            return self.grid[6]

        return None