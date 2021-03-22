

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
    for each_line in content:
      description = each_line.split()
      print(description)

  

  def get_content(self):
    return self.content