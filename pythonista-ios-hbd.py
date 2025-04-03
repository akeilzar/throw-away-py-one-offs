from scene import *
from math import sin, cos
from random import randint as r

class Game(Scene):
	def setup(self):
		self.user = [self.size.w/2,self.size.h/2]
		self.t = 0
		self.on = 1
		self.ptsize = 0.1
		self.text = 'happy birthday'
		self.evolve1 = 1
		self.texto = LabelNode('0', ('courier', 10), parent=self)
		self.texto.position = (self.size.w/2, self.size.h/2)
		self.intro = 1
	def draw(self):
		background('black')
		for i in range(10000):
			fill(r(1,100)*0.01, r(1,100)*0.01, r(1,100)*0.01)
			scale = 8
			ellipse(self.user[0]+self.user[0]*sin(self.t*self.on+i*100000)*0.9*i/100,self.user[1]+self.user[1]*cos(self.t*self.on+i*self.evolve1)*0.5*0.9*scale*i/500,self.ptsize,self.ptsize)
	def update(self):
		if self.intro > 8:
			if self.ptsize < 10:
				self.ptsize += 0.01
			if self.ptsize > 9:
				self.evolve1 += 0.1
		self.intro += 0.1
		if self.intro < 8:
			self.texto.text = self.text
		else:
			self.texto.text = ''
if __name__ == '__main__':
	run(Game(),LANDSCAPE,show_fps=True)
