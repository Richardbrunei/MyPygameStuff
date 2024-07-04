from life import life
import pygame
screen=pygame.display.set_mode([1200,600])
pygame.init()
pygame.key.set_repeat(10,10)
screen.fill([200,200,200])
clock=pygame.time.Clock()
sw=1200
sh=600
speed=1
rw=30
start=False
l=life(sw//rw,sh//rw,rw)
"""
print(l.count())
l.print()"""
def key(e):
	global speed,start
	if event.key==pygame.K_UP:
		speed*=2
	if event.key==pygame.K_DOWN:
		speed/=2
	if event.key==pygame.K_SPACE:
		start=not start
	if event.key==pygame.K_s:
		l.save()
	if event.key==pygame.K_0:
		l.cleer()
	if event.key==pygame.K_r:
		start=False
		l.rand()
	if event.key==pygame.K_1:
		l.read()
def update():
	l.draw(screen)
	if start:
		l.grow()
def onclick():
	mpos=pygame.mouse.get_pos()
	l.change(mpos[0],mpos[1])
running=True
while running:
	clock.tick(speed)
	#print(speed)
	#print(start)
	update()
	pygame.display.flip()
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running=False
		if event.type==pygame.KEYDOWN:
			key(event)
		if event.type==pygame.MOUSEBUTTONDOWN:
			onclick()
pygame.quit()