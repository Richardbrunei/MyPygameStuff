from feld import feild
from blok import blck
import pygame
w=12
h=16
l=40
pygame.init()
pygame.key.set_repeat(150,150)     #SENSITVITY
screen=pygame.display.set_mode([w*l,h*l])
clock=pygame.time.Clock()
b=blck()
f=feild(12,16,40)
fot=pygame.font.SysFont("",40)
def update():
	screen.fill([0,0,0])
	f.draw(screen,b)
	text=str(f.score)
	text=str(f.score)
	tet=fot.render(text,1,[255,255,0])
	screen.blit(tet,[0,0])
	if not f.govr():
		f.adwn(b)
		f.clear()
	else:
		print("GAME OVER")
		tex="GAME OVER"
		tet=fot.render(tex,1,[255,255,0])
		screen.blit(tet,[4*40,7*40])
	pygame.display.flip()
def key(event):
	if event.key==pygame.K_DOWN and not f.govr():
		f.movdwn(b)
	if event.key==pygame.K_LEFT and not f.govr():
		f.movlet(b)
	if event.key==pygame.K_RIGHT and not f.govr():
		f.movrit(b)
	if event.key==pygame.K_SPACE and not f.govr():
		f.rot(b)
running=True
while running:
	clock.tick(20)
	update()
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running=False
		if event.type==pygame.KEYDOWN:
			key(event)
pygame.quit()