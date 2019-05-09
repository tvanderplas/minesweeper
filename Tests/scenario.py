
import numpy as np

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

class scenario_4:

	def __init__(self):
		self.shape = (4, 4, 4)
		self.board = np.array(
			[[-1, -1, 2, 0]
			,[4, -1, 2, 0]
			,[-1, 2, 1, 0]
			,[1, 1, 0, 0]]
		)
		self.cover = np.array(
			[['', 'F', '2', '0']
			,['', 'F', '2', '0']
			,['', '2', '1', '0']
			,['', '1', '0', '0']]
		)
