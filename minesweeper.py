
import random as rd
import numpy as np

class Minesweeper(object):

	def __init__(self, width:int=30, height:int=16, mines:int=99):
		self._is_started = False
		self._win = False
		self._lose = False
		self._width = width
		self._height = height
		self._mines = mines
		self._board = np.zeros([height, width], dtype=(np.int8))
		self._cover = np.zeros([height, width], dtype=(np.str_))

	@property
	def win(self):
		return self._win

	@property
	def lose(self):
		return self._lose

	@property
	def width(self):
		return self._width

	@property
	def height(self):
		return self._height

	@property
	def view(self):
		return self._cover

	def __start(self, y, x):
		x_min = (x - 1) if x > 0 else 0
		y_min = (y - 1) if y > 0 else 0
		x_max = (x + 2) if x < self._width else x + 1
		y_max = (y + 2) if y < self._height else y + 1
		choose = np.ones([self._height, self._width], int)
		choose[y_min:y_max, x_min:x_max] = 0
		while self._mines > 0:
			toMine = np.where(choose == 1)
			m = rd.choice([i for i in zip(toMine[0], toMine[1])])
			choose[m] = 0
			if self._board[m] >= 0:
				mx_min = (m[0] - 1) if m[0] > 0 else 0
				my_min = (m[1] - 1) if m[1] > 0 else 0
				m_adj = self._board[mx_min:m[0] + 2, my_min:m[1] + 2]
				m_adj[m_adj >= 0] += 1
				self._board[m] = -1
				self._mines -= 1
		self._is_started = True

	def player_view(self):
		print(''.join(['*' * 3 * self._width]))
		print('\n'.join([' '.join([str(cell).rjust(2) for cell in row]) for row in self._cover]))
		print(''.join(['*' * 3 * self._width]))

	def full_view(self):
		print(''.join(['*' * 3 * self._width]))
		print('\n'.join([' '.join([str(cell).rjust(2) for cell in row]) for row in self._board]))
		print(''.join(['*' * 3 * self._width]))

	def __clear(self, x, y):
		x_min = (x - 1) if x > 0 else 0
		y_min = (y - 1) if y > 0 else 0
		self._cover[x, y] = str(self._board[x, y])
		if self._board[x, y] == 0:
			toClear = np.where(self._cover[x_min:x + 2, y_min:y + 2] == '')
			for i in zip(toClear[0] + x_min, toClear[1] + y_min):
				self.__clear(*i)
		if self._board[x, y] == -1:
			self._lose = True

	def clear(self, x, y):
		not_marked = np.core.defchararray.not_equal(self._cover[x, y], 'F')
		not_0 = np.core.defchararray.not_equal(self._cover[x, y], '0')
		if self._is_started == False:
			self.__start(x, y)
		if (not_marked) and (not_0) and not self._lose:
			self.__clear(x, y)

	def mark(self, x, y):
		if not self._lose:
			if np.core.defchararray.equal(self._cover[x, y], ''):
				self._cover[x, y] = 'F'
			elif np.core.defchararray.equal(self._cover[x, y], 'F'):
				self._cover[x, y] = ''

if __name__ == '__main__':
	game = Minesweeper()
	game.clear(8, 8)
