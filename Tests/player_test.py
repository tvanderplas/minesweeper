
import context
import unittest
from scenario import *
from player import Player, Minesweeper

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

	def test_get_edges_4(self):
		setup = scenario_4()
		p = Player(*setup.shape)
		p.game._board = setup.board
		p.game._cover = setup.cover
		p.game._is_started = True
		p.update()
		self.assertEqual(p.get_edges(), [(2, 1), (3, 1)])

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

	def test_get_edge_pair_4(self):
		setup = scenario_4()
		p = Player(*setup.shape)
		p.game._board = setup.board
		p.game._cover = setup.cover
		p.game._is_started = True
		p.update()
		
		self.assertEqual(p.get_edge_pair(2, 1), [(3, 1)])
		self.assertEqual(p.get_edge_pair(3, 1), [(2, 1)])

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

	def test_check_5(self):
		setup = scenario_5()
		p = Player(*setup.shape)
		p.game._board = setup.board
		p.game._cover = setup.cover
		p.game._is_started = True
		p.update()

		p.check()
		p.update()

		self.assertEqual(p.view[2, 3], 'F')
		self.assertEqual(p.view[3, 2], 'F')
		self.assertEqual(p.view[3, 3], '')

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

	def test_act_5(self):
		setup = scenario_5()
		p = Player(*setup.shape)
		p.game._board = setup.board
		p.game._cover = setup.cover
		p.game._is_started = True
		p.update()

		p.check()
		p.act()
		p.update()

		self.assertEqual(p.view[2, 3], 'F')
		self.assertEqual(p.view[3, 2], 'F')
		self.assertEqual(p.view[3, 3], '2')

	def test_study_1(self):
		setup = scenario_1()
		p = Player(*setup.shape)
		p.game._board = setup.board
		p.game._cover = setup.cover
		p.game._is_started = True
		p.update()

		p.study()
		p.update()

		self.assertEqual(p.view[0, 0], '1')
		self.assertEqual(p.view[1, 0], '')
		self.assertEqual(p.view[2, 0], '1')

	def test_study_2(self):
		setup = scenario_2()
		p = Player(*setup.shape)
		p.game._board = setup.board
		p.game._cover = setup.cover
		p.game._is_started = True
		p.update()

		p.study()
		p.update()

		self.assertEqual(p.view[0, 0], '')
		self.assertEqual(p.view[1, 0], '1')
		self.assertEqual(p.view[2, 0], '1')
		self.assertEqual(p.view[3, 0], '')

	def test_study_4(self):
		setup = scenario_4()
		p = Player(*setup.shape)
		p.game._board = setup.board
		p.game._cover = setup.cover
		p.game._is_started = True
		p.update()

		p.study()
		p.update()

		self.assertEqual(p.view[0, 0], '')
		self.assertEqual(p.view[1, 0], '4')
		self.assertEqual(p.view[2, 0], '')
		self.assertEqual(p.view[3, 0], '')

	def test_study_6(self):
		setup = scenario_6()
		p = Player(*setup.shape)
		p.game._board = setup.board
		p.game._cover = setup.cover
		p.game._is_started = True
		p.update()

		p.study()
		p.update()

		self.assertEqual(p.view[0, 3], '')
		self.assertEqual(p.view[1, 3], '1')
		self.assertEqual(p.view[2, 3], '1')
		self.assertEqual(p.view[3, 3], '1')
		self.assertEqual(p.view[4, 3], '')

if __name__ == '__main__':
	unittest.main()
