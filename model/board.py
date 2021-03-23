class Board(object):

  def __init__(self):
    self.height = 6
    self.width = 6
    self.grid = []
    self.init_grid

  def init_grid(self):
    ''' Initialize the board grid (-1 means nothing on the grid) '''
    for y in range(self.height):
      self.grid.append([])
      for x in range(self.width):
        self.grid[y].append(-1)

  def get_grid(self):
    ''' Get the board gird '''
    return self.grid

  def add_car(self, car, locations):
    ''' Add a car to the board '''
    for location in locations:
      y = location['y']
      x = location['x']
      self.grid[y][x] = car