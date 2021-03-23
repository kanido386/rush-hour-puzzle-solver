from model.car import Car
from model.board import Board
from enums.orientation import Orientation

class PuzzleLoader(object):

  def __init__(self, filename):
    self.filename = filename
    self.puzzle_board = None

    content = self.read()
    self.validate(content)
    self.parse(content)


  def read(self):
    ''' Read the puzzle file and return its content '''
    try:
      with open(self.filename, 'r') as file:
        return file.read().splitlines()
    except FileNotFoundError:
      print('Sorry! No such file!')


  @staticmethod
  def validate(self):
    ''' Validate the content of the puzzle file '''
    # Assuming that there's no bug when loading puzzle files
    pass


  def parse(self, content):
    ''' Parse the puzzle file's content into models '''
    cars = {}

    for each_line in content:
      description = each_line.split()
      # print(description)
      index = int(description[0])
      y_top_left = int(description[1])
      x_top_left = int(description[2])
      length = int(description[3])
      orientation = int(description[4])
      car = Car(index, y_top_left, x_top_left, length, orientation)
      if orientation == Orientation.HORIZONTAL:
        car.set_end_location(y_top_left, x_top_left+length-1)
      else:
        car.set_end_location(y_top_left+length-1, x_top_left)
      cars[index] = car

    self.puzzle_board = Board()
    # It will print "Car x: top-left at (x,x) and has length x, orientation x."
    # print(cars[0])
    for key, car in cars.items():
      occupied_locations = car.get_occupied_locations()
      self.puzzle_board.add_car(car, occupied_locations)


  def get_puzzle_board(self):
    ''' Get the puzzle board '''
    return self.puzzle_board


  def get_content(self):
    return self.content