from pieces.cell import Cell  

class Board:

    number_of_rows = 50
    number_of_columns = 50
    direction_dict = {
        'UP': (0, 1),
        'DOWN': (0, -1),
        'LEFT': (-1, 0),
        'RIGHT': (1, 0),
        'UP_LEFT': (-1, 1),
        'UP_RIGHT': (1, 1),
        'DOWN_LEFT': (1, -1),
        'DOWN_RIGHT': (-1, -1),
    }

    def __init__(self, rules):
        self.grid = [[Cell(x, y) for y in range(self.number_of_rows)] for x in range(self.number_of_columns)]
        self.gen = 0
        self.rules = rules

    def next_gen(self):
        # Check Neighbors
        for x in range(self.number_of_columns): # O(n)
            for y in range(self.number_of_rows): # O(n)
                temp_cell = self.grid[x][y]
                for dir_x, dir_y in self.direction_dict.values(): # O(n)
                    if x + dir_x >= 0 and y + dir_y >= 0 and x + dir_x < 50 and y + dir_y < 50:
                        temp_neighbor = self.grid[x + dir_x][y + dir_y]
                        if temp_neighbor.isAlive():
                            temp_cell.add_neighbor()
        # update grid
        for x in range(self.number_of_columns):  # O(n)
            for y in range(self.number_of_rows):  # O(n)
                self.grid[x][y].update(self.rules)

        self.gen += 1
        return self.gen

    def __str__(self):
        output = ''
        for i in range(len(self.grid)):
            output += ' '.join(map(str, self.grid[i])) + '\n'

        return output
