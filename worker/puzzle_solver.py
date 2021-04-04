from enums.direction import Direction
from enums.orientation import Orientation

from copy import deepcopy
# import itertools

class PuzzleSolver(object):

  def __init__(self, puzzle_board, algorithm, version):
    self.puzzle_board = puzzle_board
    self.algorithm = algorithm
    self.version = version

  
  def get_solution(self):

    if self.algorithm == 1:     # BFS
      print('BFS')
      return self.get_BFS_solution()

    elif self.algorithm == 2:   # DFS
      print('DFS')
      return self.get_DFS_solution()

    elif self.algorithm == 3:   # IDS
      print('IDS')
      return self.get_IDS_solution(30)

    elif self.algorithm == 4:   # A*
      print('A*')
      return self.get_A_star_solution()

    else:                       # IDA*
      print('IDA*')
      return self.get_IDA_star_solution()

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

      # print(len(moves))

      num_expanded_nodes += 1
      print(f'The number of expanded nodes: {num_expanded_nodes:>4}')

      if self.is_goal_state(grid):
        return moves

      for next_move, next_grid in self.get_next_states(grid):
        if self.version == 1:
          queue.append([moves + next_move, next_grid])
        else:
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

      # print(len(moves))

      num_expanded_nodes += 1
      print(f'The number of expanded nodes: {num_expanded_nodes:>4}')

      if self.is_goal_state(grid):
        return moves

      for next_move, next_grid in self.get_next_states(grid):
        if self.version == 1:
          stack.append([moves + next_move, next_grid])
        else:
          if hash(str(next_grid)) not in visited:
            stack.append([moves + next_move, next_grid])
            visited.add(hash(str(next_grid)))

    return None


  def get_IDS_solution(self, max_depth):
    ''' Run IDS algorithm to find the solution '''

    total_num_expanded_nodes = 0

    # d means depth
    # for d in itertools.count():
    # TODO:
    for d in range(0, max_depth, 20):
    # for d in range(max_depth):

      grid = self.puzzle_board.get_grid()
      visited = set()
      depth = 0
      start_state = [[], grid, depth]
      stack = [start_state]
      num_expanded_nodes = 0

      while len(stack) > 0:
        moves, grid, depth = stack.pop(-1)

        if self.is_goal_state(grid):
          return moves

        num_expanded_nodes += 1
        total_num_expanded_nodes += 1
        print(f'Depth {d}. The number of expanded nodes: (total) {total_num_expanded_nodes:>4}  (this level) {num_expanded_nodes:>4}')

        # limit depth
        if depth > d:
          continue
        
        for next_move, next_grid in self.get_next_states(grid):
          if self.version == 1:
            stack.append([moves + next_move, next_grid, depth + 1])
          else:
            if hash(str(next_grid)) not in visited:
              stack.append([moves + next_move, next_grid, depth + 1])
              visited.add(hash(str(next_grid)))

    return None


  @staticmethod
  def take_fourth(element):
    ''' Take the fourth element for sorting (used for sorting heuristic in list) '''
    return element[3]


  def heuristic_blocking(self, grid):
    ''' Get heuristic about cars blocking the red car '''

    heuristic = 1
    
    if self.is_goal_state(grid):
      return 0

    for x in range(6):
      y = 2
      if grid[y][x] != -1 and grid[y][x].get_index() == 0:
        x_red_car_end_location = grid[y][x].get_end_location()['x']
        break

    for x in range(x_red_car_end_location + 1, 6):
      y = 2
      if grid[y][x] != -1:
        heuristic += 1

    return heuristic



  def get_A_star_solution(self):
    ''' Run A* algorithm to find the solution '''

    grid = self.puzzle_board.get_grid()
    visited = set()
    depth = 0
    heuristic = 0
    start_state = [[], grid, depth, heuristic]
    priority_queue = [start_state]
    num_expanded_nodes = 0

    while len(priority_queue) > 0:

      # extract a node with minimal heuristic value
      priority_queue.sort(key=self.take_fourth)
      moves, grid, depth, previous_heuristic = priority_queue.pop(0)

      if self.is_goal_state(grid):
        return moves

      num_expanded_nodes += 1
      print(f'The number of expanded nodes: {num_expanded_nodes:>4} Previous heuristic: {previous_heuristic:>3}')
      
      for next_move, next_grid in self.get_next_states(grid):
        next_heuristic = self.heuristic_blocking(next_grid) + depth
        if self.version == 1:
          priority_queue.append([moves + next_move, next_grid, depth + 1, next_heuristic])
        else:
          if hash(str(next_grid)) not in visited:
            # TODO:
            # below one will speed up the process, don't know why 😂
            # (probably means don't need to take the depth into account)
            # next_heuristic = self.heuristic_blocking(next_grid)
            priority_queue.append([moves + next_move, next_grid, depth + 1, next_heuristic])
            visited.add(hash(str(next_grid)))

    return None


  def get_IDA_star_solution(self):
    ''' Run IDA* algorithm to find the solution '''

    limit = 0
    total_num_expanded_nodes = 0

    while True:

      limit += 5

      grid = self.puzzle_board.get_grid()
      visited = set()
      depth = 0
      heuristic = 0
      start_state = [[], grid, depth, heuristic]
      priority_queue = [start_state]
      num_expanded_nodes = 0

      while len(priority_queue) > 0:

        # extract a node with minimal heuristic value
        priority_queue.sort(key=self.take_fourth)
        moves, grid, depth, previous_heuristic = priority_queue.pop(0)

        if self.is_goal_state(grid):
          return moves

        total_num_expanded_nodes += 1
        num_expanded_nodes += 1
        print(f'The number of expanded nodes: (total) {total_num_expanded_nodes:>4}  (this level) {num_expanded_nodes:>4} Heuristic: {previous_heuristic:>3}')
        
        for next_move, next_grid in self.get_next_states(grid):
          next_heuristic = self.heuristic_blocking(next_grid) + depth
          # limit
          if next_heuristic > limit:
            continue
          if self.version == 1:
            priority_queue.append([moves + next_move, next_grid, depth + 1 + next_heuristic])
          else:
            if hash(str(next_grid)) not in visited:
              # TODO:
              # below one will speed up the process, don't know why 😂
              # (probably means don't need to take the depth into account)
              # next_heuristic = self.heuristic_blocking(next_grid)
              priority_queue.append([moves + next_move, next_grid, depth + 1, next_heuristic])
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