
from random import randint
from PIL import ImageGrab, Image
import numpy as np
import cv2

class Game_UI(object):

	def __init__(self, width:int=30, height:int=16, mines:int=99):
		self._width = width
		self._height = height
		self._mines = mines

	@property
	def width(self):
		return self._width

	@property
	def height(self):
		return self._height

	@property
	def mines(self):
		return self._mines

	def read(self, x, y):
		pass

	def mark(self, x, y):
		pass

	def clear(self, x, y):
		pass

def bgr_to_rgb(image: np.array):
	red = np.copy(image[::, ::, 0])
	image[::, ::, 0] = image[::, ::, 2]
	image[::, ::, 2] = red

img = np.array(ImageGrab.grab())

board_w, board_h = 30, 16
min_x, min_y, step, side = 215, 139, 50.25, 38
x_index = [min_x + round(step * x) for x in range(board_w)]
y_index = [min_y + round(step * y) for y in range(board_h)]
board = [[img[y:y + side, x:x + side] for x in x_index] for y in y_index]

for i, row in enumerate(board):
	for j, cell in enumerate(row):
		a_cell = Image.fromarray(cell[::, ::])
		# a_cell.save(str(randint(0, 99999)).zfill(5) + '.png', 'png')

bgr_to_rgb(img)
# pylint: disable=no-member
cv2.imshow("test", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# pylint: enable=no-member
