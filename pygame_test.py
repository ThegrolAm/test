import pygame as pg
import sys
pg.init()

disp = pg.display.set_mode((800, 600))
pg.display.set_caption('this is just a test	!')

BLUE = (0, 0, 255)

disp.fill(BLUE)
pg.display.update()

while True:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			sys.exit()
