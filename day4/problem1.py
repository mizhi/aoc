# https://adventofcode.com/2021/day/4


class BingoBoard:
  def __init__(self, lines):
    self._board = self._parse_lines(lines)

  def _parse_lines(self, lines):
    temp = []
    for line in lines:
      nums = line.split()
      temp.append([int(num) for num in nums])
    return temp

  def knock_out(self, ko_num):
    for i in range(len(self._board)):
      for j in range(len(self._board[i])):
        if ko_num == self._board[i][j]:
          self._board[i][j] = 'X'

  def has_bingo(self):
    for row in range(len(self._board)):
      if self._has_row_bingo(row):
        return True

    for col in range(len(self._board[0])):
      if self._has_col_bingo(col):
        return True

    return False

  def unmarked_values(self):
    values = []
    for row in range(len(self._board)):
      values.extend(val for val in self._board[row] if val != 'X')
    return values

  def _has_row_bingo(self, row):
    return all(value == 'X' for value in self._board[row])

  def _has_col_bingo(self, col):
    for row in range(len(self._board)):
      if self._board[row][col] != 'X':
        return False
    return True

  def __str__(self):
    ret = ''
    for row in self._board:
      ret += ",".join([str(num) for num in row])
      ret += '\n'
    return ret

def parse_game_file():
  with open("input.txt", "r") as f:
    all_lines = [s.strip() for s in f.readlines()]

  game_nums = [int(x) for x in all_lines[0].split(",")]

  all_boards = []
  current_board_text = []
  for line in all_lines[2:]:
    if line == "":
      if len(current_board_text) > 0:
        all_boards.append(BingoBoard(current_board_text))
        current_board_text = []
    else:
      current_board_text.append(line)
  return (game_nums, all_boards)

def find_winning_value(game_nums, all_boards):
  for game_num in game_nums:
    for board in all_boards:
      board.knock_out(game_num)
      if board.has_bingo():
        return game_num * sum(board.unmarked_values())

game_nums, all_boards = parse_game_file()

print(find_winning_value(game_nums, all_boards))
