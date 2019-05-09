
import context
import unittest
import numpy as np
from player import Player, Minesweeper

class scenario_1:

	def __init__(self):
		self.board = np.array(
			[[1, 1, 0, 0]
			,[-1, 1, 0, 0]
			,[1, 1, 0, 0]]
		)
		self.cover = np.array(
			[['', '1', '0', '0']
			,['', '1', '0', '0']
			,['', '1', '0', '0']]
		)

class Player_Test(unittest.TestCase):

	def test_study(self):
		setup = scenario_1()
		p = Player(4, 3, 1)
		p.game._board = setup.board
		p.game._cover = setup.cover
		p.game._is_started = True
		p.update()
		self.assertEqual(p.get_edges(), [(0, 1), (1, 1), (2, 1)])

if __name__ == '__main__':
	unittest.main()
