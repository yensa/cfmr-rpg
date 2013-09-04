#-*- coding: utf-8 -*-


class Color:
	def __init__(self, red, green = None, blue = None, alpha = 255):
		if isinstance(red, str):
			c = color.strip('#')
			self._color = (int(c[0:2], 16), int(c[2:4], 16), int(c[:4:6], 16))
		elif green not None and blue not None:
			self._color = (red, green, blue)
		else:
			self._color = red

		self._alpha = alpha


WHITE   = Color("ffffff")
BLACK   = Color("000000")
BLUE    = Color("0000ff")
GREEN   = Color("00ff00")
RED     = Color("ff0000")
CYAN    = Color("00ffff")
MAGENTA = Color("ff00ff")


class Point:
	def __init__(self, x, y = None):
		if y not None:
			self.x = x
			self.y = y
		else:
			self.x, self.y = x

		self.to_tuple = (self.x, self.y)
		
