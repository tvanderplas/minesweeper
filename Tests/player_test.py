
import context
import unittest
import numpy as np
from player import Player, Minesweeper

class scenario_1:

	def __init__(self):
		self.shape = (4, 3, 1)
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

class scenario_2:

	def __init__(self):
		self.shape = (4, 4, 2)
		self.board = np.array(
			[[-1, 1, 0, 0]
			,[1, 1, 0, 0]
			,[1, 1, 0, 0]
			,[-1, 1, 0, 0]]
		)
		self.cover = np.array(
			[['', '1', '0', '0']
			,['', '1', '0', '0']
			,['', '1', '0', '0']
			,['', '1', '0', '0']]
		)

class scenario_3:

	def __init__(self):
		self.shape = (4, 4, 2)
		self.board = np.array(
			[[2, -1, 1, 0]
			,[-1, 2, 1, 0]
			,[1, 1, 0, 0]
			,[0, 0, 0, 0]]
		)
		self.cover = np.array(
			[['', '', '1', '0']
			,['', '2', '1', '0']
			,['1', '1', '0', '0']
			,['0', '0', '0', '0']]
		)

class Player_Test(unittest.TestCase):

	def test_get_edges_1(self):
		setup = scenario_1()
		p = Player(*setup.shape)
		p.game._board = setup.board
		p.game._cover = setup.cover
		p.game._is_started = True
		p.update()
		self.assertEqual(p.get_edges(), [(0, 1), (1, 1), (2, 1)])

	def test_get_edges_2(self):
		setup = scenario_2()
		p = Player(*setup.shape)
		p.game._board = setup.board
		p.game._cover = setup.cover
		p.game._is_started = True
		p.update()
		self.assertEqual(p.get_edges(), [(0, 1), (1, 1), (2, 1), (3, 1)])

	def test_get_adj_val_1(self):
		setup = scenario_1()
		p = Player(*setup.shape)
		p.game._board = setup.board
		p.game._cover = setup.cover
		p.game._is_started = True
		p.update()

		self.assertEqual(p.get_adj_val(0, 0), [(1, 0)])
		self.assertEqual(p.get_adj_val(0, 1), [(0, 0), (1, 0)])
		self.assertEqual(p.get_adj_val(0, 2), [])

		self.assertEqual(p.get_adj_val(1, 0), [(0, 0), (2, 0)])
		self.assertEqual(p.get_adj_val(1, 1), [(0, 0), (1, 0), (2, 0)])
		self.assertEqual(p.get_adj_val(1, 2), [])

		self.assertEqual(p.get_adj_val(2, 0), [(1, 0)])
		self.assertEqual(p.get_adj_val(2, 1), [(1, 0), (2, 0)])
		self.assertEqual(p.get_adj_val(2, 2), [])

	def test_get_edge_pair_2(self):
		setup = scenario_2()
		p = Player(*setup.shape)
		p.game._board = setup.board
		p.game._cover = setup.cover
		p.game._is_started = True
		p.update()
		
		self.assertEqual(p.get_edge_pair(0, 1), [(1, 1), (2, 1)])
		self.assertEqual(p.get_edge_pair(1, 1), [(0, 1), (2, 1), (3, 1)])
		self.assertEqual(p.get_edge_pair(2, 1), [(0, 1), (1, 1), (3, 1)])
		self.assertEqual(p.get_edge_pair(3, 1), [(1, 1), (2, 1)])

	def test_check_3(self):
		setup = scenario_3()
		p = Player(*setup.shape)
		p.game._board = setup.board
		p.game._cover = setup.cover
		p.game._is_started = True
		p.update()

		p.check()
		p.update()

		self.assertEqual(p.view[0, 0], '')
		self.assertEqual(p.view[0, 1], 'F')
		self.assertEqual(p.view[1, 0], 'F')

	def test_act_3(self):
		setup = scenario_3()
		p = Player(*setup.shape)
		p.game._board = setup.board
		p.game._cover = setup.cover
		p.game._is_started = True
		p.update()

		p.check()
		p.act()
		p.update()

		self.assertEqual(p.view[0, 0], '2')
		self.assertEqual(p.view[0, 1], 'F')
		self.assertEqual(p.view[1, 0], 'F')

if __name__ == '__main__':
	unittest.main()
