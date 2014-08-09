import pyglet
import vector
import body
import random
import copy

window = pyglet.window.Window()
mode = 0
density = 0.5
points = []
pause = True

@window.event
def on_draw(dt=(1.0/30)):
	global mode
	global density
	global points
	global pause
	window.clear()
	modeLabel = pyglet.text.Label("Mode: {0}".format(mode))
	modeLabel.draw()
	densityLabel = pyglet.text.Label("Density: {0:.2f}".format(density), x = window.width, anchor_x = 'right')
	densityLabel.draw()
	if(pause):
		pauseLabel = pyglet.text.Label("Paused", x = window.width//2, anchor_x = 'center')
		pauseLabel.draw()
	pixel = pyglet.resource.image("pixel.png")
	for point in points:
		pixel.blit(int(point.position.x), int(point.position.y))
	new_points = copy.copy(points)
	if(not pause):
		for i in range(len(points)):
			copy_list = copy.copy(points)
			del copy_list[i]
			new_points[i].update(copy_list, dt*0.5)
		for i in range(len(new_points)):
			for j in range(i+1, len(new_points)):
				if((new_points[i].position - new_points[j].position)*(new_points[i].position - new_points[j].position) < 4):
					new_points[i], new_points[j] = body.collide(new_points[i], new_points[j])
		points = new_points

pyglet.clock.schedule_interval(on_draw, 1/30.0)

@window.event
def on_key_press(symbol, modifiers):
	global mode
	global density
	global pause
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
	if(symbol == pyglet.window.key.P):
		pause = not pause

@window.event
def on_mouse_press(x, y, button, modifiers):
	global mode
	global density
	global points
	if(button == pyglet.window.mouse.LEFT):
		if(mode == 0):
			if(density != 0):
				points.append(body.Body(position=vector.Vector(x, y), mass = 1))
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
				points.append(body.Body(position=vector.Vector(x+rand_x, y+rand_y), mass = 1))

pyglet.app.run()
