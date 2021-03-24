from enums.orientation import Orientation

class Car(object):

  def __init__(self, index, y_top_left, x_top_left, length, orientation):
    self.index = index
    self.y_top_left = y_top_left
    self.x_top_left = x_top_left
    self.start_location = { 'y': y_top_left, 'x': x_top_left }
    self.end_location = {}
    self.length = length
    self.orientation = orientation
    self.occupied_locations = []

  def get_index(self):
    return self.index

  # move_forward and move_backward currently don't update these two information

  # def get_y_top_left(self):
  #   return self.y_top_left

  # def get_x_top_left(self):
  #   return self.x_top_left

  def get_orientation(self):
    return self.orientation

  def set_start_location(self, y, x):
    ''' Set start location of the car '''
    self.start_location['y'] = y
    self.start_location['x'] = x

  def get_start_location(self):
    ''' Get start location of the car '''
    return self.start_location

  def set_end_location(self, y, x):
    ''' Set end location of the car '''
    self.end_location['y'] = y
    self.end_location['x'] = x

  def get_end_location(self):
    ''' Get end location of the car '''
    return self.end_location
  
  def move_forward(self):
    ''' Move the car forward '''
    if self.orientation == Orientation.HORIZONTAL:
      self.start_location['x'] += 1
      self.end_location['x'] += 1
    else:
      self.start_location['y'] += 1
      self.end_location['y'] += 1

  def move_backward(self):
    ''' Move the car backward '''
    if self.orientation == Orientation.HORIZONTAL:
      self.start_location['x'] -= 1
      self.end_location['x'] -= 1
    else:
      self.start_location['y'] -= 1
      self.end_location['y'] -= 1

  
  def get_occupied_locations(self):
    ''' Get and set the locations occupied by the car '''
    occupied_locations = []

    if self.orientation == Orientation.HORIZONTAL:
      for i in range(self.length):
        location = { 'y': self.start_location['y'], 'x': self.start_location['x'] + i }
        occupied_locations.append(location)
    else:
      for i in range(self.length):
        location = { 'y': self.start_location['y'] + i, 'x': self.start_location['x'] }
        occupied_locations.append(location)

    self.occupied_locations = occupied_locations
    return occupied_locations


  '''
  __repr__() 是給開發人員看的，主要用途為 debug
  '''  
  def __repr__(self):
    return f'{self.index}'
    # return f'Car {self.index}: top-left at ({self.y_top_left},{self.x_top_left}) and has length {self.length}, orientation {self.orientation}.'