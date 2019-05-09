
from minesweeper import Minesweeper
import numpy as np

class Player:

	def __init__(self, width:int=30, height:int=16, mines:int=99):
		self.width = width
		self.height = height
		self.mines = mines
		self.game = Minesweeper(self.width, self.height, self.mines)
		self.stuck = [False, False, False]

	def __i(self, a: list, b: list):
		"""return the intersection of a and b (a ∩ b)"""
		return [i for i in a if i in b]

	def __c(self, a: list, b: list):
		r"""return the complement of a and b (a \ b)"""
		return [i for i in a if i not in b]

	def unstuck(self):
		self.stuck = [False, False, False]

	def update(self):
		self.view = self.game.view

	def get_adj_val(self, x, y, value=''):
		x_min = (x - 1) if x > 0 else 0
		y_min = (y - 1) if y > 0 else 0
		x_max = (x + 2) if x < self.game.height else x + 1
		y_max = (y + 2) if y < self.game.width else y + 1
		indices = np.where(self.view[x_min:x_max, y_min:y_max] == value)
		box = [i for i in zip(indices[0] + x_min, indices[1] + y_min)]
		return self.__c(box, [(x, y)])

	def get_edge_pair(self, x, y):
		lbound = lambda a: (a - 2) if (a - 1) > 0 else 0
		ubound = lambda a, limit: (a + 3) if (a + 1) < limit else a + 1
		x_min = lbound(x)
		y_min = lbound(y)
		x_max = ubound(x, self.game.height)
		y_max = ubound(y, self.game.width)

		adj_mark = lambda a, b: len(self.get_adj_val(a, b, 'F'))
		value = lambda a, b: int(self.view[a, b]) - adj_mark(x, y)
		is_big = lambda a, b: value(x, y) >= value(a, b)

		share_unknown = lambda a, b: len(self.__i(
			self.get_adj_val(x, y), self.get_adj_val(a, b))) > 0

		indices = np.where(self.view[x_min:x_max, y_min:y_max])
		box = [i for i in zip(indices[0] + x_min, indices[1] + y_min)]
		fbox = self.__i(self.__c(box, [(x, y)]), self.get_edges())
		return [i for i in fbox if is_big(*i) and share_unknown(*i)]

	def get_edges(self):
		known = np.core.defchararray.not_equal(self.view, '')
		nonzero = np.core.defchararray.not_equal(self.view, '0')
		notmark = np.core.defchararray.not_equal(self.view, 'F')
		indices = np.where((known) & (nonzero) & (notmark))
		return [i for i in zip(*indices) if len(self.get_adj_val(*i)) > 0]

	def check(self):
		self.new_game()
		self.update()
		self.stuck[0] = True
		for cell in self.get_edges():
			adj_unk = self.get_adj_val(*cell)
			adj_mark = self.get_adj_val(*cell, 'F')
			if len(adj_unk) + len(adj_mark) == int(self.view[cell]):
				for i in adj_unk:
					self.game.mark(*i)
					self.unstuck()

	def act(self):
		self.new_game()
		self.update()
		self.stuck[1] = True
		for cell in self.get_edges():
			adj_unk = self.get_adj_val(*cell)
			adj_mark = self.get_adj_val(*cell, 'F')
			if len(adj_mark) == int(self.view[cell]):
				for i in adj_unk:
					self.game.clear(*i)
					self.unstuck()

	def study(self):
		self.new_game()
		self.update()
		self.stuck[2] = True
		for cell in self.get_edges():
			for pair in self.get_edge_pair(*cell):
				c_value = int(self.view[cell]) - len(self.get_adj_val(*cell, 'F'))
				p_value = int(self.view[pair]) - len(self.get_adj_val(*pair, 'F'))
				c_ex_p = self.__c(self.get_adj_val(*cell), self.get_adj_val(*pair))
				p_ex_c = self.__c(self.get_adj_val(*pair), self.get_adj_val(*cell))
				if c_value - p_value == len(c_ex_p):
					for i in c_ex_p:
						self.game.mark(*i)
						self.unstuck()
					for i in p_ex_c:
						self.game.clear(*i)
						self.unstuck()

	def new_game(self):
		if self.game._is_started == False:
			self.game.clear(self.height // 2, self.width // 2)

	def play(self):
		self.new_game()
		while self.game.lose == False and all(self.stuck) == False:
			while self.game.lose == False and all(self.stuck[:2]) == False:
				self.check()
				self.act()
			self.study()

	def play_series(self, games: int):
		pass

if __name__ == '__main__':
	p = Player()
	p.play()
	p.game.player_view()
