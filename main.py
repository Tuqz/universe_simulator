import pyglet
import vector
import body
import random

window = pyglet.window.Window()
mode = 0
density = 0.5
points = []

@window.event
def on_draw():
	global mode
	global density
	global points
	window.clear()
	modeLabel = pyglet.text.Label("Mode: {0}".format(mode))
	densityLabel = pyglet.text.Label("Density: {0}".format(density), x = window.width, anchor_x = 'right')
	pixel = pyglet.resource.image("pixel.png")
	for point in points:
		pixel.blit(point[0], point[1])
	modeLabel.draw()
	densityLabel.draw()

@window.event
def on_key_press(symbol, modifiers):
	global mode
	global density
	if(symbol == pyglet.window.key._1):
		mode = 1
	if(symbol == pyglet.window.key._0):
		mode = 0
	if(symbol == pyglet.window.key.PLUS):
		if(density < 1):
			density += 0.05
	if(symbol == pyglet.window.key.MINUS):
		if(density > 0):
			density -= 0.05

@window.event
def on_mouse_press(x, y, button, modifiers):
	global mode
	global density
	global points
	if(button == pyglet.window.mouse.LEFT):
		if(mode == 0):
			if(density != 0):
				points.append((x, y))
		else:
			particles = int(441*density)
			used_rands = []
			for i in range(particles):
				rand_x = random.randint(-10, 10)
				rand_y = random.randint(-10, 10)
				while((rand_x, rand_y) in used_rands):
					rand_x = random.randint(-10, 10)
					rand_y = random.randint(-10, 10)
				used_rands.append((rand_x, rand_y))
				points.append((x+rand_x, y+rand_y))

pyglet.app.run()
