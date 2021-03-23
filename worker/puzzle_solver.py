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