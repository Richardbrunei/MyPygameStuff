from random import randint
import pygame
class life(object):
	def __init__(self,w,h,rl):
		self.h=h
		self.w=w
		self.rectlen=rl
		self.life=[]
		self.rects=[]
		for i in range(h):
			b=[]
			for s in range(w):
				b.append(pygame.Rect(s*self.rectlen+1,i*self.rectlen+1,self.rectlen-1,self.rectlen-1))
			self.rects.append(b)

		for i in range(h):
			a=[]
			for s in range(w):
				a.append(randint(0,1))
			self.life.append(a)
	def count(self):
		a=0
		for i in self.life:
			for k in i:
				if k==1:
					a+=1
		return a
	def print(self):
		for i in self.life:
			for k in i:
				print(k,end=' ')
			print()
	def grow(self):
		new=[]
		for y in range(self.h):
			nr=self.life[y][:]
			for x in range(self.w):
				nb=self.countnb(x,y)
				if nb<=1:
					nr[x]=0
				if nb>3:
					nr[x]=0
				if nb==2 or nb==3:
					pass
				if nb==3:
					nr[x]=1
			new.append(nr)
		self.life=new

	def countnb(self,x,y):
		count=0
		if x>0:
			count+=self.life[y][x-1]
		if x<self.w-1:
			count+=self.life[y][x+1]
		if y>0:
			count+=self.life[y-1][x]
		if y<self.h-1:
			count+=self.life[y+1][x]
		if y<self.h-1 and x<self.w-1:
			count+=self.life[y+1][x+1]
		if y<self.h-1 and x>0:
			count+=self.life[y+1][x-1]
		if y>0 and x<self.w-1:
			count+=self.life[y-1][x-1]
		if y>0 and x>0:
			count+=self.life[y-1][x-1]
		return count
	def draw(self,screen):
		for y in range(self.h):
			for x in range(self.w):
				if self.life[y][x]==1:
					color=[255,255,255]
				else:
					color=[0,0,0]
				pygame.draw.rect(screen,color,self.rects[y][x])
	def change(self,x,y):
		for a in range(len(self.rects)):
			for b in range(len(self.rects[a])):
				if self.rects[a][b].collidepoint(x,y):
					if self.life[a][b]==0:
						self.life[a][b]=1
					elif self.life[a][b]==1:
						self.life[a][b]=0
	def save(self):
		with open("life.txt","w") as f:
			for y in self.life:
				for x in y:
					f.write(str(x))
				f.write("\n")
	def cleer(self):
		self.life=[]
		for i in range(self.h):
			a=[]
			for s in range(self.w):
				a.append(0)
			self.life.append(a)
	def rand(self):
		self.life=[]
		for i in range(self.h):
			a=[]
			for s in range(self.w):
				a.append(randint(0,1))
			self.life.append(a)
	def read(self):
		self.life=[]
		with open("life.txt","r") as f:
			for i in range(self.w):
				lin=f.readline().strip()
				linlife=[]
				for i in lin:
					num=int(i)
					linlife.append(num)
				self.life.append(linlife)