
import numpy as np

class scenario_1:

	def __init__(self):
		self.shape = (4, 3, 1)
		self.board = np.array(
			[[ 1, 1, 0, 0]
			,[-1, 1, 0, 0]
			,[ 1, 1, 0, 0]]
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
			,[ 1, 1, 0, 0]
			,[ 1, 1, 0, 0]
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
			[[ 2, -1,  1,  0]
			,[-1,  2,  1,  0]
			,[ 1,  1,  0,  0]
			,[ 0,  0,  0,  0]]
		)
		self.cover = np.array(
			[[ '',  '', '1', '0']
			,[ '', '2', '1', '0']
			,['1', '1', '0', '0']
			,['0', '0', '0', '0']]
		)

class scenario_4:

	def __init__(self):
		self.shape = (4, 4, 4)
		self.board = np.array(
			[[-1, -1,  2,  0]
			,[ 4, -1,  2,  0]
			,[-1,  2,  1,  0]
			,[ 1,  1,  0,  0]]
		)
		self.cover = np.array(
			[['', 'F', '2', '0']
			,['', 'F', '2', '0']
			,['', '2', '1', '0']
			,['', '1', '0', '0']]
		)

class scenario_5:

	def __init__(self):
		self.shape = (4, 4, 2)
		self.board = np.array(
			[[0,  0,  0,  0]
			,[0,  0,  1,  1]
			,[0,  1,  2, -1]
			,[0,  1, -1,  2]]
		)
		self.cover = np.array(
			[['0', '0', '0', '0']
			,['0', '0', '1', '1']
			,['0', '1', '2',  '']
			,['0', '1',  '',  '']]
		)

class scenario_6:

	def __init__(self):
		self.shape = (4, 5, 4)
		self.board = np.array(
			[[0,-1,-1, 1]
			,[0, 2, 2, 1]
			,[0, 1, 1, 1]
			,[0, 2,-1, 1]
			,[0,-1, 2, 1]]
		)
		self.cover = np.array(
			[['0', 'F',  '', '']
			,['0', '2',  '', '']
			,['0', '1', '1', '']
			,['0', '2',  '', '']
			,['0', 'F',  '', '']]
		)

class scenario_7:

	def __init__(self):
		self.shape = (4, 5, 6)
		self.board = np.array(
			[[0,-1,-1,-1]
			,[0, 2, 3, 2]
			,[0, 1, 1, 1]
			,[0, 2,-1, 2]
			,[0,-1, 3,-1]]
		)
		self.cover = np.array(
			[['0', 'F',  '', '']
			,['0', '2',  '', '']
			,['0', '1', '1', '']
			,['0', '2',  '', '']
			,['0', 'F',  '', '']]
		)

class scenario_8:

	def __init__(self):
		self.shape = (4, 3, 1)
		self.board = np.array(
			[[ 2, 3, 3, 2]
			,[-1,-1,-1,-1]
			,[ 2, 3, 4,-1]]
		)
		self.cover = np.array(
			[[ '', '',  '', '']
			,['F', '', 'F', '']
			,['2', '', '4', '']]
		)

if __name__ == '__main__':
	scn = scenario_5()
	print(scn.board[::-1, ::-1])
	print(scn.cover[::-1, ::-1])
