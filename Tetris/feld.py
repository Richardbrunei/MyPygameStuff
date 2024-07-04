from random import randint
import pygame
class feild():
	def __init__(self,a,b,c):
		self.w=a
		self.score=0
		self.h=b
		self.feld=[]
		self.t=0
		for i in range(b):
			f=[]
			for k in range(a):
				f.append(0)
			self.feld.append(f)
		self.l=c
		self.blok=None
		for i in range(a):
			self.feld[0][i]=3
			self.feld[b-1][i]=3
		for i in range(b):
			self.feld[i][0]=3
			self.feld[i][a-1]=3
	def draw(self,screen,b):
		for y in range(self.h):
			for x in range(self.w):
				if self.feld[y][x]==1:
					pygame.draw.rect(screen,b.color,[x*self.l,y*self.l,self.l,self.l])
				elif self.feld[y][x]==2:
					pygame.draw.rect(screen,[128,128,128],[x*self.l,y*self.l,self.l,self.l])
				elif self.feld[y][x]==3:
					pygame.draw.rect(screen,[75,75,75],[x*self.l,y*self.l,self.l,self.l])
	def set(self,x,y,wat):
		self.feld[y][x]=wat
	def movdwn(self,b):
		b.out(self)
		b.dwn()
		if not b.enter(self):
			b.up()
			b.solid(self)
	def movrit(self,b):
		b.out(self)
		b.right()
		if not b.enter(self):
			b.left()
			b.enter(self)
	def movlet(self,b):
		b.out(self)
		b.left()
		if not b.enter(self):
			b.right()
			b.enter(self)
	def collide(self,x,y):
		if y>=self.h-1:
			return True
		if x>=self.w-1:
			return True
		if x<=0:
			return True
		if self.feld[y][x]==2:
			return True
		return False
	def adwn(self,b):
		self.t+=1
		if self.t==10:
			self.movdwn(b)
			self.t=0
	def rot(self,b):
		b.out(self)
		b.rotate(),
		if not b.enter(self):
			b.rotate()
			b.enter(self)
	def govr(self):
		if 2 in self.feld[1]:
			return True
		return False
	def clear(self):
		lines=[]
		c=0
		for i in self.feld[:]:
			for k in i:
				if k==2:
					c+=1
				if c==self.w-2:
					lines.append(i)
					c=0
					break
			c=0
		if not len(lines)<=0:
			self.score+=2**(len(lines)-1)*10
		for i in lines:
			self.feld.remove(i)
			self.feld.insert(0,[0]*self.w)

		for i in range(self.h):
			for k in range(self.w):
				if self.feld[i][k]==3:
					self.feld[i][k]=0

		for i in range(self.w):
			self.feld[0][i]=3
			self.feld[self.h-1][i]=3

		for i in range(self.h):
			self.feld[i][0]=3
			self.feld[i][self.w-1]=3