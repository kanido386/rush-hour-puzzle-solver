import time
from worker.puzzle_loader import PuzzleLoader

class Solver(object):

  def __init__(self):
    self.run()

  def run(self):
    ''' Run the program '''

    # Ask user which level to play with
    print('===================================')
    print('有 01~04, 10~11, 20~31, 40 這些關卡')
    print('===================================')
    puzzle_name = input('請輸入您想要解決的關卡：')

    if puzzle_name:
      # Load puzzle from file
      filename = f'puzzle/L{puzzle_name}.txt'
      print('（讀取', filename, '中）')
      loader = PuzzleLoader(filename)
      puzzle_board = loader.get_puzzle_board()




'''
__name__ 是 Python 中內建、隱含的變數，不必宣告即可用，
當程式是直接執行時，__name__ 的值就是 __main__，
當程式是被引用時，__name__ 的值即是模組名稱
'''
if __name__ == '__main__':
  Solver()