class Cell:

    def __init__(self, x, y):
        self.state = 0
        self.alive_neighbors = 0
        self.x = x
        self.y = y

    def isAlive(self):
        if self.state == 1:
            return True
        else:
            return False

    def add_neighbor(self):
        self.alive_neighbors += 1

    def reset_neighbors(self):
        self.alive_neighbors = 0

    def update(self, rules):
        birth, low, high = list(map(int, rules.values()))
        

        if self.isAlive() and low < self.alive_neighbors > high:
            self.state = 0
        elif not self.isAlive() and self.alive_neighbors == birth:
            self.state = 1
        elif self.isAlive() and low >= self.alive_neighbors <= high:
            self.state = 1

        self.reset_neighbors()

        return self.isAlive()
    
    def __str__(self):
        if self.isAlive():
            return str(self.state)
        else:
            return ' '
