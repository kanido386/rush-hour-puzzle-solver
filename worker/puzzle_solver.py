from enums.direction import Direction
from enums.orientation import Orientation

class PuzzleSolver(object):

  def __init__(self, puzzle_board, algorithm):
    self.puzzle_board = puzzle_board
    self.algorithm = algorithm

  
  def get_solution(self):

    if self.algorithm == 1:     # BFS
      print('BFS')
      return self.get_BFS_solution()

    elif self.algorithm == 2:   # DFS
      print('DFS')

    elif self.algorithm == 3:   # IDS
      print('IDS')

    elif self.algorithm == 4:   # A*
      print('A*')

    else:                       # IDA*
      print('IDA*')

    return None


  def get_BFS_solution(self):
    ''' Run BFS algorithm to find the solution '''

    grid = self.puzzle_board.get_grid()
    start_state = [[], grid]
    queue = [start_state]

    while len(queue) > 0:
      moves, grid = queue.pop(0)

      if self.is_goal_state(grid):
        return moves

    return None


  def get_next_states(self, grid):
    ''' Get next possible states according to current state '''
    states = []

    for y in range(6):
      for x in range(6):
        car = grid[y][x]
        if car != -1:
          for direction in Direction:
            pass


  def is_goal_state(self, grid):
    ''' Check whether the puzzle board is solved '''

    # get the car on grid[2][4]
    car = grid[2][4]

    if car != -1:
      start_location = car.get_start_location()
      y = start_location['y']
      x = start_location['x']
      if (y, x) == (2, 4) and car.get_index() == 0:
        return True

    return False


  def is_movable(self, car, direction, grid):
    ''' Check whether the car can move in the given direction on current layout '''

    orientation = car.get_orientation()

    if orientation == Orientation.HORIZONTAL and direction == Direction.FORWARD:
      location = car.get_end_location()
      # new end location of the car
      y = location['y']
      x = location['x'] + 1
      previous_car = grid[y][x]
      if x >= 6 or previous_car != -1:
        return False

    elif orientation == Orientation.HORIZONTAL and direction == Direction.BACKWARD:
      location = car.get_start_location()
      # new start location of the car
      y = location['y']
      x = location['x'] - 1
      previous_car = grid[y][x]
      if x < 0 or previous_car != -1:
        return False

    elif orientation == Orientation.VERTICAL and direction == Direction.FORWARD:
      location = car.get_end_location()
      y = location['y'] + 1
      x = location['x']
      previous_car = grid[y][x]
      if y >= 6 or previous_car != -1:
        return False

    elif orientation == Orientation.VERTICAL and direction == Direction.BACKWARD:
      location = car.get_start_location()
      y = location['y'] - 1
      x = location['x']
      previous_car = grid[y][x]
      if y < 0 or previous_car != -1:
        return False

    return True