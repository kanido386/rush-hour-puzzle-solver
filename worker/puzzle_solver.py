from enums.direction import Direction
from enums.orientation import Orientation

from copy import deepcopy

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
      return self.get_DFS_solution()

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
    visited = set()
    start_state = [[], grid]
    queue = [start_state]
    num_expanded_nodes = 0

    while len(queue) > 0:
      moves, grid = queue.pop(0)

      num_expanded_nodes += 1
      print(f'The number of expanded nodes: {num_expanded_nodes:>4}')

      if self.is_goal_state(grid):
        return moves

      for next_move, next_grid in self.get_next_states(grid):
        # queue.append([moves + next_move, next_grid])
        if hash(str(next_grid)) not in visited:
          queue.append([moves + next_move, next_grid])
          visited.add(hash(str(next_grid)))

    return None


  def get_DFS_solution(self):
    ''' Run DFS algorithm to find the solution '''

    grid = self.puzzle_board.get_grid()
    visited = set()
    start_state = [[], grid]
    stack = [start_state]
    num_expanded_nodes = 0

    while len(stack) > 0:
      moves, grid = stack.pop(-1)

      num_expanded_nodes += 1
      print(f'The number of expanded nodes: {num_expanded_nodes:>4}')

      if self.is_goal_state(grid):
        return moves

      for next_move, next_grid in self.get_next_states(grid):
        # stack.append([moves + next_move, next_grid])
        if hash(str(next_grid)) not in visited:
          stack.append([moves + next_move, next_grid])
          visited.add(hash(str(next_grid)))

    return None


  def get_next_states(self, grid):
    ''' Get next possible states according to current state '''
    states = []

    for y in range(6):
      for x in range(6):
        car = grid[y][x]
        if car != -1:
          for direction in Direction:
            if self.is_movable(car, direction, grid):
              updated_grid = deepcopy(grid)
              updated_car = updated_grid[y][x]
              if direction == Direction.FORWARD:
                updated_car.move_forward()
              elif direction == Direction.BACKWARD:
                updated_car.move_backward()

              original_locations = car.get_occupied_locations()
              updated_locations = updated_car.get_occupied_locations()

              updated_grid = self.update_grid(updated_grid, updated_car, original_locations, updated_locations)
              states.append([
                # TODO:
                [[updated_car.get_index(), updated_car.get_start_location()['y'], updated_car.get_start_location()['x']]],
                updated_grid
              ])

        # For debugging
        # print('==============================')
        # for row in grid:
        #   print(row)
        # print('==============================')

    return states


  @staticmethod
  def update_grid(grid, car, original_locations, updated_locations):
    ''' Update grid with the car's new locations '''
    
    # Clear original locations
    for location in original_locations:
      y = location['y']
      x = location['x']
      grid[y][x] = -1

    # Update new locations
    for location in updated_locations:
      y = location['y']
      x = location['x']
      grid[y][x] = car

    return grid

  
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
      # previous_car = grid[y][x]
      if x >= 6 or grid[y][x] != -1:
        return False

    elif orientation == Orientation.HORIZONTAL and direction == Direction.BACKWARD:
      location = car.get_start_location()
      # new start location of the car
      y = location['y']
      x = location['x'] - 1
      # previous_car = grid[y][x]
      if x < 0 or grid[y][x] != -1:
        return False

    elif orientation == Orientation.VERTICAL and direction == Direction.FORWARD:
      location = car.get_end_location()
      y = location['y'] + 1
      x = location['x']
      # previous_car = grid[y][x]
      if y >= 6 or grid[y][x] != -1:
        return False

    elif orientation == Orientation.VERTICAL and direction == Direction.BACKWARD:
      location = car.get_start_location()
      y = location['y'] - 1
      x = location['x']
      # previous_car = grid[y][x]
      if y < 0 or grid[y][x] != -1:
        return False

    return True