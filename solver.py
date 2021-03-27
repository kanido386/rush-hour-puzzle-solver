import time
import os
from worker.puzzle_loader import PuzzleLoader
from worker.puzzle_solver import PuzzleSolver

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
    
    time.sleep(1)
    print('\n了解！\n')
    time.sleep(1)

    # Ask user which algorithm to solve with
    print('===================================')
    print('有以下五種演算法：')
    print('(1) BFS')
    print('(2) DFS')
    print('(3) IDS')
    print('(4) A*')
    print('(5) IDA*')
    print('請問您想用哪個演算法來解呀？')
    print('===================================')
    algorithm = int(input('輸入 1~5 其中一個數字：'))

    time.sleep(1)
    print('\n收到！\n')
    time.sleep(1)

    if puzzle_name:

      # Load puzzle from file
      filename = f'puzzle/L{puzzle_name}.txt'
      print('（讀取', filename, '中）')
      loader = PuzzleLoader(filename)
      puzzle_board = loader.get_puzzle_board()


      start_time = time.perf_counter()
      ''''''
      # Solve the puzzle
      solver = PuzzleSolver(puzzle_board, algorithm)
      solution = solver.get_solution()
      ''''''
      end_time = time.perf_counter()
      time_pass = end_time - start_time
      print('\n===================================\n')
      print(f'共耗時 {time_pass} 秒\n')

      if solution:

        directory = './SOLUTION'
        if not os.path.exists(directory):
          os.mkdir(directory)

        with open(f'./SOLUTION/L{puzzle_name}_solution.txt', 'w') as f:
          print('【步驟】')
          for i, step in enumerate(solution):
            print(f'{i+1:>3}:', end=' ')
            print(step)
            f.write(f'{i+1:>3}: ')
            f.write(', '.join(str(el) for el in step))
            f.write('\n')
          print(f'\n寫進 ./SOLUTION/L{puzzle_name}_solution.txt 裡囉！')





'''
__name__ 是 Python 中內建、隱含的變數，不必宣告即可用，
當程式是直接執行時，__name__ 的值就是 __main__，
當程式是被引用時，__name__ 的值即是模組名稱
'''
if __name__ == '__main__':
  Solver()