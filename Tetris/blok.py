import random
class blck():
	def __init__(self):
		self.x=5
		self.y=1
		self.dir=0
		o=[[[0,0],[0,1],[1,0],[1,1]],[[0,0],[0,1],[1,0],[1,1]],[[0,0],[0,1],[1,0],[1,1]],[[0,0],[0,1],[1,0],[1,1]]]
		i=[[[-1,0],[0,0],[1,0],[2,0]],[[0,-1],[0,0],[0,1],[0,2]],[[-1,0],[0,0],[1,0],[2,0]],[[0,-1],[0,0],[0,1],[0,2]]]
		t=[[[-1,0],[0,0],[1,0],[0,1]],[[-1,0],[0,0],[0,-1],[0,1]],[[0,0],[1,0],[-1,0],[0,-1]],[[0,0],[0,-1],[0,1],[1,0]]]
		l=[[[-1,0],[0,0],[1,0],[-1,-1]],[[-1,1],[0,0],[0,-1],[0,1]],[[-1,0],[1,0],[0,0],[1,1]],[[0,0],[0,1],[0,-1],[-1,-1]]]
		j=[[[-1,0],[0,0],[1,0],[-1,1]],[[0,-1],[0,0],[0,1],[1,1]],[[-1,0],[0,0],[1,0],[1,-1]],[[0,0],[-1,-1],[0,-1],[0,1]]]
		s=[[[-1,0],[0,0],[0,-1],[1,-1]],[[-1,-1],[-1,0],[0,0],[0,1]],[[-1,1],[0,0],[0,1],[1,0]],[[0,0],[0,-1],[1,0],[1,1]]]
		z=[[[1,0],[0,0],[0,-1],[-1,-1]],[[-1,0],[-1,1],[0,0],[0,-1]],[[0,0],[-1,0],[0,1],[1,1]],[[0,0],[0,1],[1,0],[1,-1]]]
		self.shapes=[o,i,t,l,j,s,z]
		ff=random.choice(self.shapes)
		self.shape=ff
		self.points=ff[0]
		index=self.shapes.index(self.shape)
		self.colors=[[0,128,0],[200,0,0],[0,0,250],[200,128,250],[250,128,200],[205,152,252],[200,112,3]]
		self.color=self.colors[index]
	def setxy(self,x,y):
		self.x=x
		self.y=y
	def enter(self,feld):
		for p in self.points:
			if feld.collide(self.x+p[0],self.y+p[1]):
				print("x:",self.x)
				print("y:",self.y)
				print()
				return False
		for p in self.points:
			feld.set(self.x+p[0],self.y+p[1],1)
		print("x:",self.x)
		print("y:",self.y)
		print()
		return True
	def dwn(self):
		self.y+=1
	def out(self,feld):
		for p in self.points:
			print(type(p[0]),type(p[1]))
			feld.set(self.x+p[0],self.y+p[1],0)
	def rotate(self):
		self.dir+=1
		if self.dir==4:
			self.dir=0
		self.points=self.shape[self.dir]
	def up(self):
		self.y-=1
	def left(self):
		self.x-=1
	def right(self):
		self.x+=1
	def solid(self,feld):
		for p in self.points:
			feld.set(self.x+p[0],self.y+p[1],2)
		ff=random.choice(self.shapes)
		self.shape=ff
		self.points=ff[0]
		index=self.shapes.index(self.shape)
		self.color=self.colors[index]
		self.x=5
		self.y=1
		self.dir=0